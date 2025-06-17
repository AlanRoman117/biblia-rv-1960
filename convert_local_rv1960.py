import os
import json
import ast # For safely evaluating string tuples

def transform_rv1960_to_kjv_structure():
    source_dir = 'bible-json-master/origen/' # UPDATED
    output_dir = 'rv1960_output'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    all_books_list = []
    book_chapter_counts = {}

    if not os.path.exists(source_dir):
        print(f"--- ERROR ---")
        print(f"Source directory not found at: '{source_dir}'")
        return

    source_files = sorted([f for f in os.listdir(source_dir) if f.endswith('.txt')]) # UPDATED to .txt
    
    print(f"Found {len(source_files)} .txt files in '{source_dir}'. Starting processing...")

    for filename in source_files:
        filepath = os.path.join(source_dir, filename)
        
        # Derive book_name from filename
        book_name_base = filename[:-4] # Remove .txt
        if "_" in book_name_base:
            parts = book_name_base.split('_')
            # Capitalize first letter of each part for names like "1_corintios" -> "1 Corintios"
            # However, for simple names like "genesis", it should just be "Genesis"
            if len(parts) > 1 and parts[0].isdigit() and not parts[1][0].isdigit(): # Handles "1_corintios", "2_reyes"
                 book_name = parts[0] + " " + parts[1].capitalize()
            # Handles cases like song_of_solomon -> Song Of Solomon
            elif len(parts) > 1 and not parts[0].isdigit() :
                 book_name = " ".join(p.capitalize() for p in parts)
            # Fallback for other cases like "job" or if format is unexpected, just capitalize first part
            else:
                 book_name = parts[0].capitalize()
                 if len(parts) > 1: # if there are other parts, append them capitalized
                     book_name += " " + " ".join(p.capitalize() for p in parts[1:])

        else: # For single-word names like "genesis"
            book_name = book_name_base.capitalize()

        print(f"Processing {book_name} from {filename}...")

        kjv_structured_book = {
            "book": book_name,
            "chapters": []
        }
        
        chapters_data_collector = {} # To collect verses under chapter numbers

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line_number, line_content in enumerate(f, 1):
                    line_content = line_content.strip()
                    if not line_content:
                        continue # Skip empty lines
                    
                    try:
                        # Remove potential trailing comma 
                        processed_line = line_content
                        if processed_line.endswith(','):
                            processed_line = processed_line[:-1]
                        
                        # Handle lines that might be part of a larger list (e.g. if file is not one tuple per line)
                        # For this script, we assume one tuple per line is the dominant format.
                        # ast.literal_eval is safer than eval()
                        parsed_tuple = ast.literal_eval(processed_line)
                        
                        if not isinstance(parsed_tuple, tuple):
                            print(f"Warning: Skipping malformed line in {filename} line {line_number}: Expected a tuple, but got {type(parsed_tuple)}. Line: '{line_content[:100]}...'")
                            continue

                        if len(parsed_tuple) == 4:
                            _book_id, chapter_num, verse_num, verse_text = parsed_tuple
                            
                            if not (isinstance(chapter_num, int) and 
                                    isinstance(verse_num, int) and 
                                    isinstance(verse_text, str)):
                                print(f"Warning: Skipping malformed data in {filename} line {line_number}: Unexpected types in tuple {parsed_tuple}")
                                continue

                            chapter_verses = chapters_data_collector.setdefault(chapter_num, [])
                            chapter_verses.append({"verse": verse_num, "text": verse_text})
                        else:
                            print(f"Warning: Skipping malformed line in {filename} line {line_number}: Expected 4 elements in tuple, got {len(parsed_tuple)}. Tuple: {parsed_tuple}")
                    except (SyntaxError, ValueError) as e:
                        print(f"Warning: Skipping malformed line in {filename} line {line_number}. Error: {e}. Line: '{line_content[:100]}...'")
                        continue
        except Exception as e:
            print(f"Error reading or processing file {filepath}: {e}")
            continue # Skip this file

        # Assemble chapters from collected data, ensuring verses are sorted
        sorted_chapter_keys = sorted(chapters_data_collector.keys())
        for chapter_num in sorted_chapter_keys:
            verses = sorted(chapters_data_collector[chapter_num], key=lambda v: v['verse'])
            kjv_structured_book["chapters"].append({
                "chapter": chapter_num,
                "verses": verses
            })
        
        if not kjv_structured_book["chapters"]:
            print(f"Warning: No chapters found or processed for {book_name} from {filename}. Skipping output for this book.")
            continue

        all_books_list.append(book_name) 
        book_chapter_counts[book_name] = len(kjv_structured_book["chapters"])

        # Sanitize book_name for filename (e.g., "1 Juan" -> "1_Juan.json")
        output_filename_base = book_name.replace(" ", "_") 
        output_filename = os.path.join(output_dir, f"{output_filename_base}.json")
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            json.dump(kjv_structured_book, f_out, ensure_ascii=False, indent=4)

    if all_books_list:
        all_books_list.sort() # Sort alphabetically
        books_json_path = os.path.join(output_dir, 'books.json')
        with open(books_json_path, 'w', encoding='utf-8') as f:
            json.dump(all_books_list, f, ensure_ascii=False, indent=4)
        print("\nCreated books.json")

        # Sort book_chapter_counts by book name for consistent output
        sorted_book_chapter_counts = {k: book_chapter_counts[k] for k in sorted(book_chapter_counts.keys())}
        book_chapter_counts_path = os.path.join(output_dir, 'book_chapter_counts.json')
        with open(book_chapter_counts_path, 'w', encoding='utf-8') as f:
            json.dump(sorted_book_chapter_counts, f, ensure_ascii=False, indent=4)
        print("Created book_chapter_counts.json")
    else:
        print("\nNo books were processed successfully. 'books.json' and 'book_chapter_counts.json' not created.")
    
    print("\n--- Transformation complete! ---")
    print(f"All processed files have been saved in the '{output_dir}' directory.")

if __name__ == '__main__':
    transform_rv1960_to_kjv_structure()

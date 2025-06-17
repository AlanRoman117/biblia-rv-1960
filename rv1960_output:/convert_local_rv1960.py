import os
import json

def transform_rv1960_to_kjv_structure():
    """
    Reads Reina Valera 1960 Bible data from the manually created 
    'bible-json-master' directory, transforms it, and saves the
    new JSON files to the 'rv1960_output' directory.
    """
    # --- UPDATED to match your folder name ---
    source_dir = 'bible-json-master/books'
    output_dir = 'rv1960_output'
    
    # Check if the output directory exists, create it if not.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    all_books_list = []
    book_chapter_counts = {}

    # Verify the source directory exists before proceeding.
    if not os.path.exists(source_dir):
        print(f"--- ERROR ---")
        print(f"Source directory not found at: '{source_dir}'")
        print("Please make sure the 'bible-json-master' folder is in the same directory as this script.")
        return

    # List all json files in the source directory
    source_files = sorted([f for f in os.listdir(source_dir) if f.endswith('.json')])
    
    print(f"Found {len(source_files)} book files in '{source_dir}'. Starting processing...")

    # Process each book file
    for filename in source_files:
        filepath = os.path.join(source_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            book_data = json.load(f)

        book_name = book_data.get('name')
        if not book_name:
            print(f"Skipping file {filename} as it does not contain a 'name' key.")
            continue
            
        print(f"Processing {book_name}...")

        kjv_structured_book = {
            "book": book_name,
            "chapters": []
        }

        chapters_data = book_data.get('chapters', [])
        
        for i, chapter_content in enumerate(chapters_data, 1):
            verses_list = chapter_content.get('verses', [])
            chapter_verses = [
                {"verse": j, "text": verse_text}
                for j, verse_text in enumerate(verses_list, 1)
            ]
            kjv_structured_book["chapters"].append({
                "chapter": i,
                "verses": chapter_verses
            })
        
        all_books_list.append(book_name)
        book_chapter_counts[book_name] = len(chapters_data)

        # Write the structured JSON file for the book
        output_filename = os.path.join(output_dir, f"{book_name}.json")
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            json.dump(kjv_structured_book, f_out, ensure_ascii=False, indent=4)

    # Create books.json
    books_json_path = os.path.join(output_dir, 'books.json')
    with open(books_json_path, 'w', encoding='utf-8') as f:
        json.dump(all_books_list, f, ensure_ascii=False, indent=4)
    print("\nCreated books.json")

    # Create book_chapter_counts.json
    book_chapter_counts_path = os.path.join(output_dir, 'book_chapter_counts.json')
    with open(book_chapter_counts_path, 'w', encoding='utf-8') as f:
        json.dump(book_chapter_counts, f, ensure_ascii=False, indent=4)
    print("Created book_chapter_counts.json")
    
    print("\n--- Transformation complete! ---")
    print(f"All files have been saved in the '{output_dir}' directory.")


if __name__ == '__main__':
    transform_rv1960_to_kjv_structure()
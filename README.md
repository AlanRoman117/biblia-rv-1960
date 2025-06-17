# Reina Valera 1960 Bible in JSON Format

This repository provides the complete, generated text of the Spanish Reina Valera 1960 (RV1960) Bible in a clean, structured JSON format. It is designed for developers and anyone who needs easy, programmatic access to the scriptures.

The data structure is modeled after the popular `aruljohn/Bible-kjv` project to ensure consistency and ease of use for developers familiar with that format.

## How to Use the Files

The directory contains the final, generated JSON files. You can directly use these files in your projects without needing to run any scripts.

## Data Structure

The data is organized into the following files within the `rv1960_output/` directory:

1.  **Individual Book Files (66 files):** Each book of the Bible has its own JSON file (e.g., `Génesis.json`, `Apocalipsis.json`). The structure of each file is:

    ```json
    {
      "book": "Génesis",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "verse": 1,
              "text": "En el principio creó Dios los cielos y la tierra."
            },
            {
              "verse": 2,
              "text": "Y la tierra estaba desordenada y vacía..."
            }
          ]
        }
      ]
    }
    ```

2.  **`books.json`:** A simple JSON array containing the names of all 66 books in alphabetical order.

    ```json
    [
        "1 Crónicas",
        "1 Corintios",
        "1 Juan",
        ...
    ]
    ```

3.  **`book_chapter_counts.json`:** A JSON object mapping each book's name to its total number of chapters.

    ```json
    {
      "Génesis": 50,
      "Éxodo": 40,
      "Levítico": 27,
      ...
    }
    ```

## Credits and Source

* **Source Text Data:** The original plain text data for the Reina Valera 1960 was sourced from the `josevladimir/bible-json` repository.
* **JSON Structure Model:** This project's output format is based on the structure of the `aruljohn/Bible-kjv` repository to provide a familiar and easy-to-use API for developers.

## License

This project is released under the **MIT License**. See the `LICENSE` file for more details.

---

# Biblia Reina Valera 1960 en Formato JSON

Este repositorio proporciona el texto completo y ya generado de la Biblia Reina Valera 1960 (RV1960) en un formato JSON limpio y estructurado. Está diseñado para desarrolladores y cualquier persona que necesite un acceso fácil y programático a las escrituras.

La estructura de datos está modelada a partir del popular proyecto `aruljohn/Bible-kjv` para asegurar la consistencia y facilidad de uso para los desarrolladores familiarizados con ese formato.

## Cómo Usar los Archivos

El directorio contiene los archivos JSON finales y generados. Puede usar estos archivos directamente en sus proyectos sin necesidad de ejecutar ningún script.

## Estructura de Datos

Los datos están organizados en los siguientes archivos dentro del directorio `rv1960_output/`:

1.  **Archivos de Libros Individuales (66 archivos):** Cada libro de la Biblia tiene su propio archivo JSON (p. ej., `Génesis.json`, `Apocalipsis.json`). La estructura de cada archivo es:

    ```json
    {
      "book": "Génesis",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "chapter": 1,
              "text": "En el principio creó Dios los cielos y la tierra."
            },
            {
              "verse": 2,
              "text": "Y la tierra estaba desordenada y vacía..."
            }
          ]
        }
      ]
    }
    ```

2.  **`books.json`:** Un arreglo JSON simple que contiene los nombres de los 66 libros en orden alfabético.

    ```json
    [
        "1 Crónicas",
        "1 Corintios",
        "1 Juan",
        ...
    ]
    ```

3.  **`book_chapter_counts.json`:** Un objeto JSON que mapea el nombre de cada libro con su número total de capítulos.

    ```json
    {
      "Génesis": 50,
      "Éxodo": 40,
      "Levítico": 27,
      ...
    }
    ```

## Créditos y Fuente

* **Datos del Texto Fuente:** Los datos originales en texto plano para la Reina Valera 1960 se obtuvieron del repositorio `josevladimir/bible-json`.
* **Modelo de Estructura JSON:** El formato de salida de este proyecto se basa en la estructura del repositorio `aruljohn/Bible-kjv` para proporcionar una API familiar y fácil de usar para los desarrolladores.

## Licencia

Este proyecto se publica bajo la **Licencia MIT**. Consulte el archivo `LICENSE` para más detalles.
import ast
import pandas as pd

"""
Module: clean_utils
Summary: Utilities for cleaning and normalizing data fields.
Description: Provides helper functions to sanitize and normalize raw string inputs,
             making them easier to process downstream (ETL, analytics, model training).

Swagger/OpenAPI:
  tags:
    - name: Data Cleaning
      description: Helpers to clean raw fields from datasets.
"""


def clean_studio_format(entry):
    """
    Summary:
        Normalize a 'studios' field from string representations like "['Studio Name']" into a clean studio name.
    Description:
        Converts a string containing a Python list literal (e.g., "['Studio Name']") into a real list,
        then returns the first studio name if available. Non-string or invalid inputs return None.

    Parameters:
        entry (str | Any): The raw studios field, typically a stringified list.

    Returns:
        str | None: The normalized studio name, or None if the input is invalid or empty.

    Swagger/OpenAPI:
      operationId: cleanStudioFormat
      tags:
        - Data Cleaning
      parameters:
        - name: entry
          in: body
          required: true
          schema:
            type: string
            nullable: true
          description: Raw studios value (stringified list; e.g., "['Studio Name']").
      responses:
        '200':
          description: Successfully normalized studio name.
          schema:
            type: string
            nullable: true
        '400':
          description: Invalid input format; returns null.
      examples:
        request:
          entry: "['Bones']"
        response:
          value: "Bones"
    """
    try:
        # Se è null o non è una stringa, lo ignoriamo
        if pd.isna(entry) or not isinstance(entry, str):
            return None

        # Converte la stringa "['Nome']" in una lista vera ['Nome']
        # ast.literal_eval è sicuro per valutare strutture dati da stringhe
        lista_studi = ast.literal_eval(entry)

        # Se la conversione ha successo ed è una lista non vuota
        if isinstance(lista_studi, list) and len(lista_studi) > 0:
            return lista_studi[0]  # Restituisce il primo elemento

        return None
    except (ValueError, SyntaxError):
        # Se c'è un errore di parsing, ritorna None
        return None
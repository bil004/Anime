import ast
import pandas as pd

"""
Module: clean_utils
Utilities for data cleaning and normalization.

Provides helper functions to sanitize and normalize raw string inputs,
facilitating downstream exploratory data analysis (EDA), ETL pipelines, and modeling.
"""


def clean_studio_format(entry):
    """
    Extracts the primary production studio from a string representation of a list.

    Normalizes string values like "['Studio Name']" by parsing them into actual
    Python lists and returning the first available studio name. Useful for preprocessing
    columns containing stringified data structures within DataFrames.

    Parameters:
        entry (str | Any): Raw value from the studios field (e.g., "['Bones']").

    Returns:
        str | None: Extracted studio name, or None if the input is invalid or empty.
    """
    try:
        if pd.isna(entry) or not isinstance(entry, str):
            return None

        # Convert the string "['Name']" into a real list ['Name']
        # ast.literal_eval safely evaluates data structures from strings
        lista_studi = ast.literal_eval(entry)

        # If conversion is successful and yields a non-empty list
        if isinstance(lista_studi, list) and len(lista_studi) > 0:
            return lista_studi[0]

        return None
    except (ValueError, SyntaxError):
        return None
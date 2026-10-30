from sqlalchemy import Engine
import pandas as pd

"""
Module: readSaveCsv
I/O utilities for loading and persisting datasets to SQL databases.

Provides helper functions to read database tables directly into Pandas DataFrames
and save processed data analysis results back into the database.
"""


def import_data(engine: Engine, table: str):
    """
    Loads the full contents of a database table into a Pandas DataFrame.

    Parameters:
        engine (sqlalchemy.Engine): SQLAlchemy Engine instance for database connection.
        table (str): Target table name in the database.

    Returns:
        pandas.DataFrame | None: DataFrame containing table data, or None if an error occurs.
    """
    try:
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, engine)

        print(f"Successo: Dati letti correttamente.")
        return df

    except Exception as e:
        print(f"Errore durante l'esportazione dal DB: {e}")
        return None


def save_data(df: pd.DataFrame, file: str, engine: Engine):
    """
    Writes a Pandas DataFrame to a database table.

    Uses `to_sql` with overwrite mode (`if_exists="replace"`) to persist
    cleaned or transformed data directly into the target database table.

    Parameters:
        df (pandas.DataFrame): The DataFrame to persist.
        file (str): Destination table name in the database.
        engine (sqlalchemy.Engine): SQLAlchemy Engine instance for database connection.

    Returns:
        None
    """
    try:
        df.to_sql(file, engine, if_exists="replace", index=False)
        print(f"Successo: {len(df)} righe caricate nella tabella '{file}'.")

    except Exception as e:
        print(f"Errore durante il caricamento nel DB: {e}")
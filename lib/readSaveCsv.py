from sqlalchemy import Engine
import pandas as pd

"""
Module: readSaveCsv
Summary: Helpers to import data from the database and save DataFrames back to tables.
Description: Wraps common read/write operations using SQLAlchemy Engines and pandas.

Swagger/OpenAPI:
  tags:
    - name: I/O
      description: Database read and write utilities using pandas and SQLAlchemy.
"""


def import_data(engine: Engine, table: str):
    """
    Summary:
        Read the full contents of a database table into a pandas DataFrame.
    Description:
        Executes a SELECT * query against the given table using the provided SQLAlchemy Engine.
        Returns a DataFrame or None if an error occurs.

    Parameters:
        engine (sqlalchemy.Engine): A SQLAlchemy Engine instance.
        table (str): The name of the table to read.

    Returns:
        pandas.DataFrame | None: DataFrame with table contents, or None on failure.

    Swagger/OpenAPI:
      operationId: importData
      tags:
        - I/O
      parameters:
        - name: engine
          in: body
          required: true
          schema:
            type: object
            description: SQLAlchemy Engine (opaque).
        - name: table
          in: body
          required: true
          schema:
            type: string
          description: Target table name to read from.
      responses:
        '200':
          description: Data loaded successfully.
          schema:
            type: array
            items:
              type: object
        '500':
          description: Database read error; returns null.
      examples:
        request:
          table: "public.anime"
    """
    try:
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, engine)

        print(f"Successo: Dati letti correttamente.")
        return df

    except Exception as e:
        print(f"Errore durante l'esportazione dal DB: {e}")
        return None


def save_data(df, file, engine):
    """
    Summary:
        Save a pandas DataFrame to a database table (replace if exists).
    Description:
        Uses pandas.to_sql with if_exists="replace" to upload the DataFrame to the specified table.
        Returns None and prints a status message; logs errors on failure.

    Parameters:
        df (pandas.DataFrame): The DataFrame to persist.
        file (str): The destination table name.
        engine (sqlalchemy.Engine): A SQLAlchemy Engine instance.

    Returns:
        None

    Swagger/OpenAPI:
      operationId: saveData
      tags:
        - I/O
      parameters:
        - name: df
          in: body
          required: true
          schema:
            type: array
            items:
              type: object
          description: DataFrame rows to be stored.
        - name: file
          in: body
          required: true
          schema:
            type: string
          description: Destination table name.
        - name: engine
          in: body
          required: true
          schema:
            type: object
            description: SQLAlchemy Engine (opaque).
      responses:
        '204':
          description: Data saved successfully (no content).
        '500':
          description: Database write error.
      examples:
        request:
          file: "public.anime_clean"
    """
    try:
        df.to_sql(file, engine, if_exists="replace", index=False)
        print(f"Successo: {len(df)} righe caricate nella tabella '{file}'.")

    except Exception as e:
        print(f"Errore durante il caricamento nel DB: {e}")

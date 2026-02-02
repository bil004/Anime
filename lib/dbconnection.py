from dotenv import load_dotenv
from sqlalchemy import create_engine
from pathlib import Path
import os

"""
Module: dbconnection
Summary: Database configuration and connection helpers.
Description: Loads environment-based configuration and creates SQLAlchemy Engines for connecting to PostgreSQL.

Swagger/OpenAPI:
  tags:
    - name: Database
      description: Configuration and connection utilities for the database.
"""

BASE_DIR = Path(__file__).resolve().parent.parent

# CONFIGURAZIONE
db_config = {
    'user': '',
    'password': '',
    'host': '',
    'port': 0,
    'database': ''
}

def load_config(path=BASE_DIR / '.env'):
    """
    Summary:
        Load database configuration from a .env file into the global db_config dict.
    Description:
        Reads DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME from the provided .env path
        and populates the db_config dictionary.

    Parameters:
        path (Path | str): Path to the .env file (default: project root .env).

    Returns:
        None

    Swagger/OpenAPI:
      operationId: loadDbConfig
      tags:
        - Database
      parameters:
        - name: path
          in: query
          required: false
          schema:
            type: string
          description: Filesystem path to the .env file.
      responses:
        '204':
          description: Configuration loaded (no content returned).
      examples:
        request:
          path: "C:/project/.env"
    """
    load_dotenv(path)
    db_config['user'] = os.getenv('DB_USER')
    db_config['password'] = os.getenv('DB_PASS')
    db_config['host'] = os.getenv('DB_HOST')
    db_config['port'] = os.getenv('DB_PORT')
    db_config['database'] = os.getenv('DB_NAME')


def create_db_engine(path=BASE_DIR / '.env'):
    """
    Summary:
        Create a SQLAlchemy Engine for PostgreSQL using environment configuration.
    Description:
        Loads configuration via load_config, then builds a PostgreSQL connection URL
        and returns a SQLAlchemy Engine instance.

    Parameters:
        path (Path | str): Path to the .env file used to load config.

    Returns:
        sqlalchemy.Engine: A SQLAlchemy engine bound to the configured PostgreSQL database.

    Swagger/OpenAPI:
      operationId: createDbEngine
      tags:
        - Database
      parameters:
        - name: path
          in: query
          required: false
          schema:
            type: string
          description: Filesystem path to the .env file.
      responses:
        '200':
          description: Engine created successfully.
          schema:
            type: object
            description: SQLAlchemy Engine (opaque).
      examples:
        request:
          path: "C:/project/.env"
    """
    load_config(path)
    db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    return create_engine(db_url)
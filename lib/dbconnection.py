from dotenv import load_dotenv
from sqlalchemy import create_engine
from pathlib import Path
import os

"""
Module: dbconnection
Database configuration and connection management.

Loads environment variables and creates SQLAlchemy Engine instances to establish
connections to PostgreSQL databases within data analysis workflows.
"""

BASE_DIR = Path(__file__).resolve().parent.parent

# CONFIGURATION
db_config = {
    'user': '',
    'password': '',
    'host': '',
    'port': 0,
    'database': ''
}


def load_config(path=BASE_DIR / '.env'):
    """
    Loads database connection parameters from an environment file (.env).

    Reads DB_USER, DB_PASS, DB_HOST, DB_PORT, and DB_NAME from the specified .env file
    and populates the global `db_config` dictionary.

    Parameters:
        path (Path | str): Path to the .env file (default: project root).

    Returns:
        None
    """
    load_dotenv(path)
    db_config['user'] = os.getenv('DB_USER')
    db_config['password'] = os.getenv('DB_PASS')
    db_config['host'] = os.getenv('DB_HOST')
    db_config['port'] = os.getenv('DB_PORT')
    db_config['database'] = os.getenv('DB_NAME')


def create_db_engine(path=BASE_DIR / '.env'):
    """
    Creates a SQLAlchemy Engine for connecting to PostgreSQL.

    Initializes configuration settings via `load_config` and constructs the database
    connection URI required for integration with pandas or other analysis tools.

    Parameters:
        path (Path | str): Path to the .env file for loading configuration parameters.

    Returns:
        sqlalchemy.Engine: Ready-to-use SQLAlchemy Engine instance.
    """
    load_config(path)
    db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    return create_engine(db_url)
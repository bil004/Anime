from dotenv import load_dotenv
from sqlalchemy import create_engine
from pathlib import Path
import os


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
    load_dotenv(path)
    db_config['user'] = os.getenv('DB_USER')
    db_config['password'] = os.getenv('DB_PASS')
    db_config['host'] = os.getenv('DB_HOST')
    db_config['port'] = os.getenv('DB_PORT')
    db_config['database'] = os.getenv('DB_NAME')

    # for key, value in db_config.items():
    #     print(f"{key}: {value}")


def create_db_engine(path=BASE_DIR / '.env'):
    load_config(path)
    db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    return create_engine(db_url)
from sqlalchemy import Engine
import pandas as pd


def load_csv_file(engine: Engine, table: str):
    try:
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, engine)

        print(f"Successo: Dati letti correttamente.")
        return df

    except Exception as e:
        print(f"Errore durante l'esportazione dal DB: {e}")
        return None


def save_csv_file(df, file, engine):
    try:
        df.to_sql(file, engine, if_exists="replace", index=False)
        print(f"Successo: {len(df)} righe caricate nella tabella '{file}'.")

    except Exception as e:
        print(f"Errore durante il caricamento nel DB: {e}")

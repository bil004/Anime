import pandas as pd
import duckdb as dd
import os

# Usare chunk + Dtypes per ottimizzare la lettura

def load_csv_file(file):
    return pd.read_csv(file)

def save_csv_file(df, file):
    results = []
    if not os.path.exists('../../cleaned_data'):
        os.makedirs('../../cleaned_data')

    df.to_csv(file)
    print(f"DataFrame saved to {file}")



def query_big_files(file, query):
    con = dd.connect("../../cleaned_data/big_data.db")
    res = con.execute(query).df()
    print(res)

    return res
import pandas as pd
import os

def load_csv_file(file):
    df = pd.read_csv(file)
    return df

def save_csv_file(df, file):
    if not os.path.exists('../../cleaned_data'):
        os.makedirs('../../cleaned_data')

    df.to_csv(file, index=False)
    print(f"DataFrame saved to {file}")
import pandas as pd
from pathlib import Path

def load_data(path):
    return pd.read_excel(path)

def clean_data(df):
    df.drop_duplicates(inplace=True)

    df.fillna(df.mean(numeric_only=True), inplace=True)

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip().str.title()

    return df

def save_data(df, output):
    output_path = Path(output).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_excel(output_path, index=False)

    print(f"✅ File saved at: {output_path}")
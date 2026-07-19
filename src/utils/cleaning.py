import pandas as pd

def remove_duplicates(df):
    "'"
    "Remove duplicatas do DataFrame."""
    return df.drop_duplicates()

def strip_text_columns(df):
    """Remove espaços em branco das colunas de texto do DataFrame."""
    text_columns = df.select_dtypes(include="object").columns
    for col in text_columns:
        df[col] = df[col].str.strip()
    return df

def convert_datetime(df, date_columns):
    """Converte colunas de data para o tipo datetime."""
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    return df
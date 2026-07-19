from src.config import PROCESSED_DATA

def save_csv(df, filename):
    PROCESSED_DATA.mkdir(exist_ok=True)
    df.to_csv(PROCESSED_DATA / filename, index=False)
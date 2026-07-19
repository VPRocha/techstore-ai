from pathlib import Path
import pandas as pd
from src.config import RAW_DATA

def extract_csv(filename):
    return pd.read_csv(RAW_DATA / filename)
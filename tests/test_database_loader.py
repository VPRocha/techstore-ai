import pandas as pd

from src.config import PROCESSED_DATA
from src.database.loader import load_dataframe


customers = pd.read_csv(PROCESSED_DATA / "customers.csv")

load_dataframe(
    customers,
    "customers",
    customers.columns.tolist()
)
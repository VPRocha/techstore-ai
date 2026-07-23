import pandas as pd

from src.config import PROCESSED_DATA
from src.database.loader import load_dataframe


def populate_customers():
    print("Carregando customers...")

    customers = pd.read_csv(PROCESSED_DATA / "customers.csv")

    load_dataframe(
        customers,
        "customers",
        customers.columns.tolist()
    )


def populate_orders():
    print("Carregando orders...")

    orders = pd.read_csv(
    PROCESSED_DATA / "orders.csv",
        parse_dates=[
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ],
    )

    load_dataframe(
        orders,
        "orders",
        orders.columns.tolist()
    )


def main():

    print("=" * 50)
    print("Populando banco de dados...")
    print("=" * 50)

    populate_customers()
    populate_orders()

    print("=" * 50)
    print("Banco populado com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()
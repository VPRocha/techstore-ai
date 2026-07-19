from src.utils.cleaning import (
    remove_duplicates,
    strip_text_columns,
    convert_datetime,
)

def transform_customers(df):
    """Transforma o DataFrame de clientes."""
    df = remove_duplicates(df)
    df = strip_text_columns(df)
    df["customer_city"] = df["customer_city"].str.title()
    df["customer_state"] = df["customer_state"].str.upper()
    return df

def transform_orders(df):
    """Transforma o DataFrame de pedidos."""
    df = remove_duplicates(df)
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    df = convert_datetime(df, date_columns)

    return df

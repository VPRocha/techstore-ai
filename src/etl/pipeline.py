from src.etl.extract import extract_csv
from src.etl.transform import transform_customers, transform_orders
from src.etl.load import save_csv
from src.utils.logger import logger


def main():

    logger.info("========== Iniciando Pipeline ETL ==========")

    # Customers
    logger.info("Lendo tabela customers...")
    customers = extract_csv("olist_customers_dataset.csv")

    logger.info(f"{len(customers)} registros carregados.")

    customers = transform_customers(customers)

    save_csv(customers, "customers.csv")

    logger.info("Customers processados com sucesso.")

    # Orders
    logger.info("Lendo tabela orders...")
    orders = extract_csv("olist_orders_dataset.csv")

    logger.info(f"{len(orders)} registros carregados.")

    orders = transform_orders(orders)

    save_csv(orders, "orders.csv")

    logger.info("Orders processados com sucesso.")

    logger.info("========== Pipeline finalizado ==========")


if __name__ == "__main__":
    main()
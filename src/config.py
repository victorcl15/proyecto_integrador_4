from pathlib import Path
from typing import Dict

# DATASET_ROOT_PATH: 
# Convierte en cadena de texto la ruta absoluta al directorio "dataset", que se encuentra dos niveles arriba del archivo actual.
DATASET_ROOT_PATH = str(Path(__file__).parent.parent / "dataset")

# QUERIES_ROOT_PATH: 
# Define la ruta absoluta al directorio "queries", ubicado dos niveles arriba del archivo actual.
QUERIES_ROOT_PATH = str(Path(__file__).parent.parent / "queries")

# QUERY_RESULTS_ROOT_PATH: 
# Establece la ruta absoluta al directorio "tests/query_results", donde se almacenan los resultados de las consultas,
# y se encuentra dos niveles arriba del archivo actual.
QUERY_RESULTS_ROOT_PATH = str(Path(__file__).parent.parent / "tests/query_results")

# PUBLIC_HOLIDAYS_URL: 
# URL de la API que proporciona información sobre días festivos públicos.
PUBLIC_HOLIDAYS_URL = "https://date.nager.at/api/v3/publicholidays"

# SQLITE_BD_ABSOLUTE_PATH: 
# Define la ruta absoluta al archivo de base de datos SQLite ("olist.db"), ubicado dos niveles arriba del archivo actual.
SQLITE_BD_ABSOLUTE_PATH = str(Path(__file__).parent.parent / "olist.db")


def get_csv_to_table_mapping() -> Dict[str, str]:
    # Esta función devuelve un diccionario que mapea los nombres de archivos CSV a los nombres de las tablas
    # en la base de datos. Las claves del diccionario son los nombres de los archivos CSV y los valores,
    # los nombres de las tablas correspondientes.
    
    #Returns:
    #    Dict[str, str]: Dictionary with keys as the csv file names and
    #    values as the table names.
    #"""
    return dict(
        [
            # Mapea "olist_customers_dataset.csv" a la tabla "olist_customers"
            ("olist_customers_dataset.csv", "olist_customers"),
            # Mapea "olist_geolocation_dataset.csv" a la tabla "olist_geolocation"
            ("olist_geolocation_dataset.csv", "olist_geolocation"),
            # Mapea "olist_order_items_dataset.csv" a la tabla "olist_order_items"
            ("olist_order_items_dataset.csv", "olist_order_items"),
            # Mapea "olist_order_payments_dataset.csv" a la tabla "olist_order_payments"
            ("olist_order_payments_dataset.csv", "olist_order_payments"),
            # Mapea "olist_order_reviews_dataset.csv" a la tabla "olist_order_reviews"
            ("olist_order_reviews_dataset.csv", "olist_order_reviews"),
            # Mapea "olist_orders_dataset.csv" a la tabla "olist_orders"
            ("olist_orders_dataset.csv", "olist_orders"),
            # Mapea "olist_products_dataset.csv" a la tabla "olist_products"
            ("olist_products_dataset.csv", "olist_products"),
            # Mapea "olist_sellers_dataset.csv" a la tabla "olist_sellers"
            ("olist_sellers_dataset.csv", "olist_sellers"),
            # Mapea "product_category_name_translation.csv" a la tabla "product_category_name_translation"
            (
                "product_category_name_translation.csv",
                "product_category_name_translation",
            ),
        ]
    )

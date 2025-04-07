import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from src.extract import extract
from src import config

def extract_data():
    """
    Extrae datos de archivos CSV y API de días festivos.
    Reutiliza la función extract del proyecto original.
    """
    csv_folder = config.DATASET_ROOT_PATH
    public_holidays_url = config.PUBLIC_HOLIDAYS_URL
    csv_table_mapping = config.get_csv_to_table_mapping()
    
    print("🔄 Iniciando extracción de datos...")
    csv_dataframes = extract(csv_folder, csv_table_mapping, public_holidays_url)
    print("✅ Extracción completada exitosamente")
    
    return csv_dataframes

if __name__ == "__main__":
    extract_data()
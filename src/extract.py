from typing import Dict

import requests
from pandas import DataFrame, read_csv, read_json, to_datetime
import pandas as pd

def temp() -> DataFrame:
    """Get the temperature data.
    Returns:
        DataFrame: A dataframe with the temperature data.
    """
    return read_csv("data/temperature.csv")

def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    """Get the public holidays for the given year for Brazil.
    Args:
        public_holidays_url (str): url to the public holidays.
        year (str): The year to get the public holidays for.
    Raises:
        SystemExit: If the request fails.
    Returns:
        DataFrame: A dataframe with the public holidays.
    """
    # TODO: Implementa esta función.
    # Debes usar la biblioteca requests para obtener los días festivos públicos del año dado.
    # La URL es public_holidays_url/{year}/BR.
    # Debes eliminar las columnas "types" y "counties" del DataFrame.
    # Debes convertir la columna "date" a datetime.
    # Debes lanzar SystemExit si la solicitud falla. Investiga el método raise_for_status
    # de la biblioteca requests.
    url = f"{public_holidays_url}/{year}/BR"
    try:
        # Realiza la petición HTTP GET a la URL
        response = requests.get(url)
        # Verifica que la respuesta sea exitosa
        response.raise_for_status()
        
        # Convierte la respuesta JSON a DataFrame
        holidays_df = pd.DataFrame(response.json())
        
        # Elimina las columnas 'types' y 'counties' si están presentes
        if 'types' in holidays_df.columns:
            holidays_df.drop(columns='types', inplace=True)
        if 'counties' in holidays_df.columns:
            holidays_df.drop(columns='counties', inplace=True)
        
        # Convierte la columna 'date' a tipo datetime
        holidays_df['date'] = pd.to_datetime(holidays_df['date'])
        
        return holidays_df
    except requests.RequestException as e:
        # Imprime el error y termina el proceso si la solicitud falla
        print(f"Failed to fetch public holidays: {e}")
        raise SystemExit(e)


def extract(csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str) -> Dict[str, DataFrame]:
    """
    Extrae los datos de los archivos CSV y los carga en dataframes.
    
    Args:
        csv_folder (str): Ruta a la carpeta que contiene los archivos CSV.
        csv_table_mapping (Dict[str, str]): Diccionario que mapea nombres de archivos CSV a nombres de tablas.
        public_holidays_url (str): URL desde la que se obtendrán los días festivos públicos.
    
    Returns:
        Dict[str, DataFrame]: Diccionario con nombres de tablas como claves y dataframes como valores.
    """
    # Crea un diccionario de dataframes:
    # Para cada par (nombre del archivo CSV, nombre de la tabla) en csv_table_mapping,
    # lee el archivo CSV y lo asigna al nombre de la tabla correspondiente.
    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")  # Lee el archivo CSV ubicado en la ruta especificada.
        for csv_file, table_name in csv_table_mapping.items()  # Itera sobre cada elemento del mapeo.
    }

    # Obtiene los días festivos públicos para el año 2017 desde la URL proporcionada.
    holidays = get_public_holidays(public_holidays_url, "2017")

    # Agrega el dataframe de días festivos al diccionario bajo la clave "public_holidays".
    dataframes["public_holidays"] = holidays

    # Retorna el diccionario que contiene todos los dataframes.
    return dataframes

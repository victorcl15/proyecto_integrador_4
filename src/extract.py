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


def extract(
    csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str
) -> Dict[str, DataFrame]:
    """Extract the data from the csv files and load them into the dataframes.
    Args:
        csv_folder (str): The path to the csv's folder.
        csv_table_mapping (Dict[str, str]): The mapping of the csv file names to the
        table names.
        public_holidays_url (str): The url to the public holidays.
    Returns:
        Dict[str, DataFrame]: A dictionary with keys as the table names and values as
        the dataframes.
    """
    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()
    }

    holidays = get_public_holidays(public_holidays_url, "2017")

    dataframes["public_holidays"] = holidays

    return dataframes

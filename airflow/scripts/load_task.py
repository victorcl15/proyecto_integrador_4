import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from sqlalchemy import create_engine
from src.load import load
from src import config

def load_data(dataframes=None):
    """
    Carga los dataframes en la base de datos SQLite.
    Reutiliza la función load del proyecto original.
    
    Args:
        dataframes: Diccionario de dataframes para cargar en la base de datos.
                    Si es None, se obtienen de la tarea anterior.
    """
    # Crear conexión a la base de datos
    engine = create_engine(f"sqlite:///{config.SQLITE_BD_ABSOLUTE_PATH}", echo=False)
    
    # Si se proporcionan dataframes, los cargamos
    if dataframes:
        print("🔄 Iniciando carga de datos en la base de datos...")
        load(data_frames=dataframes, database=engine)
        print("✅ Carga completada exitosamente")
        
    return True

if __name__ == "__main__":
    load_data()
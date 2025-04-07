import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from sqlalchemy import create_engine
from src.transform import run_queries
from src import config

def transform_data():
    """
    Ejecuta las consultas de transformación en la base de datos.
    Reutiliza la función run_queries del proyecto original.
    """
    # Crear conexión a la base de datos
    engine = create_engine(f"sqlite:///{config.SQLITE_BD_ABSOLUTE_PATH}", echo=False)
    
    print("🔄 Iniciando transformaciones de datos...")
    query_results = run_queries(database=engine)
    print("✅ Transformaciones completadas exitosamente")
    
    return True

if __name__ == "__main__":
    transform_data()
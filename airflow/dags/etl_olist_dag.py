from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Añadir la ruta del proyecto para poder importar los scripts
dag_path = os.path.dirname(os.path.abspath(__file__))
airflow_path = os.path.dirname(dag_path)
project_path = os.path.dirname(airflow_path)
sys.path.append(project_path)
sys.path.append(airflow_path)

from scripts.extract_task import extract_data
from scripts.load_task import load_data
from scripts.transform_task import transform_data

# Definir argumentos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Crear el DAG
with DAG(
    'etl_olist_pipeline',
    default_args=default_args,
    description='Pipeline ELT para datos de Olist E-commerce',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['olist', 'ecommerce', 'etl'],
) as dag:

    # Tarea 1: Extraer datos
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    # Tarea 2: Cargar datos a SQLite
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        op_kwargs={'dataframes': None},  # Se pasa None para que Airflow use XCom
        provide_context=True,
    )

    # Tarea 3: Transformar datos
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    # Definir dependencias
    extract_task >> load_task >> transform_task
from airflow.operators.empty import EmptyOperator
from airflow.decorators import dag
from airflow.operators.python import PythonOperator

from airflow import DAG
import json

from datetime import datetime

import requests


def extract_data(url, ti):
    res = requests.get(url)
    json_data = json.loads(res.data)
    ti.xcom_push(key='extracted_users', value=json_data)


def load_data(user):
    print(user)


with DAG(
    dag_id='data-merge',
    schedule_interval='@daily',
    start_date=datetime(2023, 6, 4)
) as dag:
    task_get_data = PythonOperator(
        task_id='extract_users',
        python_callable=extract_data,
        op_kwargs={'url': 'http://country.io/names.json'}
    )
    task_load_data = PythonOperator(
        task_id='load_users',
        python_callable=load_data,
        op_kwargs={'path': '/home/airflow/airflow/data/users.csv'}
    )

    task_get_data >> task_load_data

from airflow.operators.empty import EmptyOperator
from airflow.decorators import dag


import json

from datetime import datetime

import requests


def extract_data(url, ti):
    res = requests.get(url)
    json_data = json.loads(res.data)
    ti.xcom_push(key='extracted_users', value=json_data)


@dag(start_date=datetime(2023, 2, 4, 10, 5), schedule='@daily')
def generateDag():
    EmptyOperator(task_id="country")


generateDag()

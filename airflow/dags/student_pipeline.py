from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

import requests

FASTAPI_URL = "http://fastapi:8000"

def create_student():

    student = {
        "name": "John",
        "email": "john@test.com",
        "age": 24
    }

    response = requests.post(
        f"{FASTAPI_URL}/students/",
        json=student
    )

    print(response.json())

def get_students():

    response = requests.get(
        f"{FASTAPI_URL}/students/"
    )

    print(response.json())


default_args = {
    "owner": "airflow",
}

with DAG(

    dag_id="student_pipeline",

    start_date=datetime(2025, 1, 1),

    schedule="@hourly",

    catchup=False,

    default_args=default_args,

    tags=["kafka", "fastapi"],

) as dag:

    create_student_task = PythonOperator(
        task_id="create_student",
        python_callable=create_student,
    )

    get_students_task = PythonOperator(
        task_id="get_students",
        python_callable=get_students,
    )

    create_student_task >> get_students_task
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello from Airflow!")

with DAG(
    dag_id="hello_arxiv_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["test"],
) as dag:
    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=say_hello,
    )

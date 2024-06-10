from airflow import DAG 

from airflow.utils.dates import days_ago

from airflow.operators.python_operator import PythonOperator

dag = DAG( 

        dag_id = "print_airflow_context",
        start_date = days_ago(1),
        schedule = None,
        description='A simple tutorial DAG to print airflow context',
)

def print_context(**kwargs):
    for k , v in kwargs.items():
        print("the keys" , k )
        print("The values" , v)

PythonOperator(
    task_id = 'print_context',
    python_callable = print_context,
    dag = dag
)

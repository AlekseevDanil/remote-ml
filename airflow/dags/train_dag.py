from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "admin",
    "start_date": days_ago(1),  # launch a day ago
    "retries": 5,  # repeat the launch a maximum of 5 times on error
    "task_concurency": 1  # only 1 task at a time
}

piplines = {'train': {"schedule": "1 * * * *"}}  # At 20:39 on Saturday MSK

def init_dag(dag, task_id):
    with dag:
        t1 = BashOperator(
            task_id=f"{task_id}",
            bash_command=f'python3 ../{task_id}.py'
        )
    return dag

for task_id, params in piplines.items():
    # DAG - acyclic graph
    dag = DAG(
        task_id,
        schedule_interval=params['schedule'],
        max_active_runs=1,
        default_args=default_args
    )
    init_dag(dag, task_id)
    globals()[task_id] = dag

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'hadoop',
    'start_date': datetime(2023, 10, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Create an instance of the DAG
dag = DAG(
    'task_to_run',
    default_args=default_args,
    description='Data pipeline for collecting and analyzing data from Mastadon',
    schedule_interval=timedelta(minutes=1),
    catchup=False,
)

# Run Task to get data
run_get_data = BashOperator(
    task_id='run_get_data_task',
    bash_command="python3 /home/hadoop/Mastadon/Data_Collection.py",
    dag=dag,
)

# Task to run the Reducer script

run_mapreducer = BashOperator(
    task_id='run_mapreducer_task',
    bash_command="python3 /home/hadoop/Mastadon/MapReduce.py /home/hadoop/Mastadon/mastodon_data..json > /home/hadoop/Mastadon/output.txt",
    dag=dag,
)

run_inset_hbase = BashOperator(
    task_id='insert_into_hbase',
    bash_command='python3 /home/hadoop/Mastadon/connection.py',
    dag=dag
)

# Set task dependencies
run_get_data >> run_mapreducer >> run_inset_hbase

if __name__ == "__main__":
    dag.cli()
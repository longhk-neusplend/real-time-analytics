# Required library
from airflow import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup
from airflow.utils.dates import days_ago
from airflow.providers.apache.kafka.operators.produce import ProduceToTopicOperator
from airflow.providers.apache.kafka.operators.consume import ConsumeFromTopicOperator
from airflow.operators.dummy import DummyOperator
import random
import json
import datetime

default_args = {
    'owner':'Kim Long',
    'start_date': days_ago(1),
}

def read_data_id():
    with open("/opt/airflow/dags/data_id_keep_track", "r") as f:
        data_id = int(f.readline())
        return data_id

def write_data_id(data_id):
    with open("/opt/airflow/dags/data_id_keep_track", "w") as f:
        f.write(str(data_id) + "\n")

def extract_bitcoin_json():
    coin_names = ["bitcoin", "ethereum", "litecoin", "ripple", "bitcoin-cash", "dogecoin", "cardano", "polkadot", "chainlink", "stellar"]

    # Get the data_id value and update data_id
    data_id = read_data_id()
    write_data_id(data_id + 1)
    
    for coin_name in coin_names:
        coin_data = {}

        # Get data ID
        coin_data["data_id"] = data_id

        # Get name
        coin_data["coin_name"] = coin_name

        # Get datetime
        current_date_time = datetime.datetime.now() 
        coin_data["timestamp"] = current_date_time.strftime("%Y-%m-%dT%H:%M:%S")

        # Get price
        price = round(random.uniform(0, 100000), 2)
        coin_data["coin_price"] = price

        yield (json.dumps(data_id),json.dumps(coin_data))
    

with DAG('Coins_Price_ETL', schedule_interval='*/4 * * * *',
         default_args=default_args, catchup=False) as dag:
    t1 = ProduceToTopicOperator(
        task_id="produce_to_topic",
        topic="coins_topic_offical",
        kafka_config_id="kafka_default",
        producer_function=extract_bitcoin_json,
    )

    start = DummyOperator(task_id='Start')
    loaded = DummyOperator(task_id='All_data_loaded')
    end = DummyOperator(task_id='End')

    start >> t1 >> loaded >> end
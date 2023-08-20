from airflow import DAG
from airflow.decorators import task
from airflow.utils.task_group import TaskGroup
from airflow.utils.dates import days_ago
from airflow.providers.apache.kafka.operators.produce import ProduceToTopicOperator
from airflow.providers.apache.kafka.operators.consume import ConsumeFromTopicOperator
from datetime import datetime
import json
import logging

default_args = {
    'owner':'Kim Long',
    'start_date': days_ago(1),
}

fruits_test = ["Apple", "Pear", "Peach", "Banana"]
def producer_function():
    for i in fruits_test:
        yield (json.dumps(i), json.dumps(i + i))

consumer_logger = logging.getLogger("airflow")
def consumer_function(message, prefix=None):
    key = json.loads(message.key())
    value = json.loads(message.value())
    consumer_logger.info(f"{prefix} {message.topic()} @ {message.offset()}; {key} : {value}")
    return

with DAG('test_kafka_connection', schedule_interval='@once',
         default_args=default_args, catchup=False) as dag:
    
    t1 = ProduceToTopicOperator(
        task_id="produce_to_topic",
        topic="coins_topic",
        kafka_config_id="kafka_default",
        producer_function=producer_function,
        )
    
    t2 = ConsumeFromTopicOperator(
        task_id="consume_from_topic",
        topics=["coins_topic"],
        kafka_config_id="kafka_default",
        apply_function=consumer_function,
        apply_function_kwargs={"prefix": "consumed:::"},
        commit_cadence="never",
        max_messages=10,
        max_batch_size=2,
    )

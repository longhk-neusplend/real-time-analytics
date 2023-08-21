# Real Time Analytic With Druid - Airflow - Kafka - Superset
[![Kafka](https://img.shields.io/badge/kafka-latest-green)](https://kafka.apache.org/documentation/)
[![Airflow](https://img.shields.io/badge/airflow-2.6.3-green)](https://airflow.apache.org/docs/)
[![Druid](https://img.shields.io/badge/druid-26.0.0-orange)](https://druid.apache.org/docs/latest/design/)
[![Redis](https://img.shields.io/badge/redis-latest-orange)](https://redis.io/)
[![Posgresql](https://img.shields.io/badge/postgres-13-brown)](https://www.postgresql.org/)
[![Superset](https://img.shields.io/badge/Superset-'latest-dev'-lightgrey)](https://superset.apache.org/docs/intro/)

This project gives an introduction to setting up streaming analytics using open source technologies. We'll use Apache {Kafka, Superset, Druid, Airflow} to set up a system that allows you to get a deeper understanding of the behaviour of your customers. [Apache Druid](https://github.com/apache/druid)

## Screenshots & Gifs

**View System**

<div>
    <kbd>
        <img title="View System" src="https://github.com/longhk-neusplend/real-time-analytics/blob/master/public/chart.png?raw=true" />
    </kbd>
    <br/>
</div>
<br>

## Contents
- [Screenshots & Gifs](#screenshots--gifs)
- [Example](#example)
    - [1. Install docker, docker-compose](https://docs.docker.com/compose/install/)
    - [2. Pull git repo](https://github.com/longhk-neusplend/real-time-analytics.git)
    - [3. Start Server](https://github.com/longhk-neusplend/real-time-analytics#3-start-server)
- [Contact Us](#contact-us)


## Example

### 1. Install docker and docker-compose

`https://www.docker.com/`

### 2. Pull git repo
`git clone https://github.com/longhk-neusplend/real-time-analytics.git` 

### 3. Start Server
`cd real-time-analytics && docker-compose up`

| Service               | URL                              | User/Password                                 |
| :-------------------: | :------------------------------: | :-------------------------------------------: |
| Druid Unified Console | http://localhost:8888/           | None                                          |
| Druid Legacy Console  | http://localhost:8081/           | None                                          |
| Superset              | http://localhost:8088/           | docker exec -it superset bash superset-init   |
| Airflow               | http://localhost:8080/           | airflow/standalone_admin_password.txt   |

### 3. Create Dashboard sample from druid streaming
 - Airflow dags at airflow/dags/demo.py each one min sent message to kafka 'demo' topic with data of list coin ["bitcoin", "ethereum", "litecoin", "ripple", "bitcoin-cash", "dogecoin", "cardano", "polkadot", "chainlink", "stellar"] the structure of data message like below.
```
   {
        "data_id" : 454,
        "coin_name": 'BTC',
        "timestamp": '2021-02-05T10:10:01',
        "coin_price": 34567
    }
```

 - From druid load data from kafka ```kafka:9092```, choice ```demo``` topic and config data result table
<div>
    <img src="./public/druid_connect.gif" />
</div>
<br>

 - From superset add druid like database sqlalchemy uri: ```druid://broker:8082/druid/v2/sql/```. more detail at [Superset-Database-Connect](https://superset.apache.org/docs/databases/db-connection-ui)
 - Create Chart and dashboard on superset from ```demo``` table.
 - Completed!

## Contact Us
- Business Email: long.hk@neusplend.com - Henry Hoang
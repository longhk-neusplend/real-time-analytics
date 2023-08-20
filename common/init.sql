-- create airflow and airflow
CREATE DATABASE airflow;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

-- create druid and druid
CREATE DATABASE druid;
CREATE USER druid WITH PASSWORD 'FoolishPassword';
GRANT ALL PRIVILEGES ON DATABASE druid TO druid;

-- create superset db and user
CREATE DATABASE superset;
CREATE USER superset WITH PASSWORD 'superset';
GRANT ALL PRIVILEGES ON DATABASE superset TO superset;

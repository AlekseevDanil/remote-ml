FROM python:3.8

# Create a working directory
WORKDIR /airflow

ENV AIRFLOW_HOME=~/airflow
ENV AIRFLOW_VERSION=2.1.1
ENV PYTHON_VERSION=3.8

RUN pip install apache-airflow==2.1.1 psycopg2-binary==2.9.1\
	--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.1.1/constraints-3.8.txt"

EXPOSE 8080
CMD ["airflow", "webserver"]

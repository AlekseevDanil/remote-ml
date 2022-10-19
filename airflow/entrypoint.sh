#!/bin/sh

rm -rf /root/airflow/dags/.ipynb_checkpoints

airflow db init

airflow scheduler \
  & exec airflow webserver --pid /tmp/airflow.pid

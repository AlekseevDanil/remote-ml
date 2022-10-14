FROM python:3.9-slim

# Create a working directory
WORKDIR /airflow

RUN pip install "apache-airflow==2.4.1" \
	--constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.4.1/constraints-3.9.txt"

EXPOSE 8080
RUN airflow standalone
CMD ["airflow", "standalone"]

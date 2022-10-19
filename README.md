# Assembly under ML for remote servers

![python](https://img.shields.io/badge/3.8-python-blue?logo=python&logoColor=white)
![airflow](https://img.shields.io/badge/2.1.1-airflow-green?logo=Apache%20Airflow&logoColor=white)
![jupyterlab](https://img.shields.io/badge/3.4.8-jupyter-orange?logo=jupyter&logoColor=white)

## Overview
For machine learning, you often have to use clouds or remote servers. And so I made this assembly for quick initialization of machines and packaged it all in Docker.

## Installing
- First, clone this repository on your working machine and go to it. ([How to use GitHub + SSH?](https://gist.github.com/AlekseevDanil/8a9999fdf520074f49db30ff34f28615))

```bash
$ git clone git@github.com:AlekseevDanil/remote-ml.git
$ cd remote-ml
```

- Before starting the second step, make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/) installed. Then proceed with the following commands.\
You need to create an **.env** file that will contain all the virtual environment variables we need.

```bash
$ touch .env
```

- Next, add the following to the **.env** file. Change the values to your. Make sure the ports you specify are free.

```bash
POSTGRES_USER="airflow"
POSTGRES_PASSWORD="airflow"
POSTGRES_DB="airflow"
POSTGRES_HOST="postgres"
POSTGRES_PORT=5432
AIRFLOW_PORT=8080
JUPYTER_PORT=6060
```

- Now we raise our docker images.\
--build means we will build our images based on Dockerfiles\
-d means bring up in the background without explicitly showing logging

```bash
$ docker-compose up --build -d
```

- And the final installation step is to create a user for our airflow.\
We go inside the airflow container and write the command to create a user (specify your data)

```bash
$ docker exec -it airflow bash

$ airflow users create \
      --username admin \
      --password 12345 \
      --firstname Admin \
      --lastname Admin \
      --role Admin \
      --email admin@admin.com

$ exit
```

## Completion

Congratulations to everyone who has made it this far! 🎉

### Jupyter Lab
If you ran all the commands and everything went up without errors, then you can now go to *your_host:6060* and you will see a window welcoming Jupyter Lab.

To get the secret key, go to the terminal and enter this command, after that there will be similar links at the very top, they contain the key we need.

```bash
$ docker logs jupyterlab
```

Copy what is highlighted in the screenshot\
<img src="https://i.pinimg.com/564x/45/f9/01/45f90171f06c4713becc06753629e629.jpg" width="550">

Yes, there is a dark theme!\
<img src="https://i.pinimg.com/564x/2f/77/16/2f7716c06339b1353ac8cd2ae5ce2b12.jpg" width="400">

### Airflow
In order to see airflow, you need to go to the browser along the path *your_host:8080*\
Next, enter the username and password you provided earlier.

This is what it looks like after logging in\
<img src="https://i.pinimg.com/564x/1c/f8/30/1cf830c789d57f7b406898dbb06a1df2.jpg" width="400">
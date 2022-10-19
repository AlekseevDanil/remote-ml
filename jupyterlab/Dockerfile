FROM python:3.9

# Create a working directory
WORKDIR /jupyterlab

# Installing the required dependencies
RUN apt-get update
RUN apt-get install build-essential libpq-dev python3-dev ffmpeg libsm6 libxext6 libgl1-mesa-glx -y
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install jupyterlab==3.4.8

# Run app
EXPOSE 6060
CMD ["jupyter", "lab", "--no-browser", "--ip=0.0.0.0", "--port=6060", "--allow-root"]

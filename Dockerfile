FROM python:3.8
WORKDIR ~/Desktop/imagesToS3/project

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

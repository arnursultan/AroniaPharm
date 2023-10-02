FROM python:latest
LABEL authors="ar_nursultan"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /AroniaPharm
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . .

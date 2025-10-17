FROM python:3.13-slim

RUN apt-get update -y && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    libczmq-dev \
    libssl-dev \
    inetutils-telnet \
    bind9utils \
    gcc \
    && apt-get clean

RUN pip install mlflow[extras]==3.4.0
RUN pip install mysqlclient
RUN pip install boto3

EXPOSE 8080

WORKDIR /app

RUN chmod -R 777 /app

USER 1001

ENTRYPOINT ["mlflow", "server"]
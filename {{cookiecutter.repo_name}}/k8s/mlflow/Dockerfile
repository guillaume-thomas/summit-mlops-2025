FROM python:3.13-slim

ARG USER_UID=1014080000

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

RUN pip install mlflow[extras]
RUN pip install mysqlclient
RUN pip install boto3

EXPOSE 8080

RUN useradd -u ${USER_UID} -m appuser
RUN mkdir -p /app
RUN mkdir -p /app/mlruns
RUN chmod -R 777 /app

WORKDIR /app

USER ${USER_UID}

ENTRYPOINT ["mlflow", "server"]
FROM python:3.13-slim

ARG USER_UID=1014080000
ARG MLFLOW_S3_ENDPOINT_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV MLFLOW_S3_ENDPOINT_URL=${MLFLOW_S3_ENDPOINT_URL} \
    AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
    AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}

ENV GIT_PYTHON_REFRESH=quiet

RUN useradd -u ${USER_UID} -m appuser
RUN mkdir -p /app && chown ${USER_UID}:${USER_UID} /app

WORKDIR /app

RUN pip install --no-cache-dir uv
COPY --chown=${USER_UID}:${USER_UID} pyproject.toml uv.lock README.md ./
COPY --chown=${USER_UID}:${USER_UID} src ./src

USER ${USER_UID}

RUN uv sync -n --no-group api --group training

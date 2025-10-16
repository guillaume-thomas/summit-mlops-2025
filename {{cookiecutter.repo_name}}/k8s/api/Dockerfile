FROM python:3.13-slim

ARG USER_UID=1014080000

RUN useradd -u ${USER_UID} -m appuser
RUN mkdir -p /app && chown ${USER_UID}:${USER_UID} /app

WORKDIR /app

RUN pip install --no-cache-dir uv
COPY --chown=${USER_UID}:${USER_UID} pyproject.toml uv.lock README.md ./
COPY --chown=${USER_UID}:${USER_UID} ./src/{{ cookiecutter.module_name }}/api ./src/{{ cookiecutter.module_name }}/api

USER ${USER_UID}

RUN uv sync -n --no-group training --group api

EXPOSE 8080

ENTRYPOINT ["uv", "run", "api"]
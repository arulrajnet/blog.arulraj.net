ARG VARIANT="3.12"
ARG POETRY_VERSION="1.8.3"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

RUN pip install poetry ${POETRY_VERSION}

ENV PATH="${PATH}:/workspace/.venv/bin"

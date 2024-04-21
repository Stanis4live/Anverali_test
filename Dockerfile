FROM python:3.11
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . /app/
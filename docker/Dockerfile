FROM python:3.12-slim

# Set environment variables to avoid .pyc files and enable faster output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential curl && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-interaction --without dev

COPY src/ src/
COPY docker/start.sh .

RUN chmod +x start.sh

CMD ["./start.sh"]

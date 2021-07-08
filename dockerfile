FROM python:3.7-slim-buster as base

# Perform common operations, dependency installation etc...
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"

RUN mkdir TO-DO-APP

WORKDIR /TO-DO-APP

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false --local && poetry install
COPY . .
    
# Configuration for local development
FROM base as development
EXPOSE 5000
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]


# Configuration for production
FROM base as production
EXPOSE 5000
ENTRYPOINT ["poetry", "run", "gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]

FROM python:3.7-slim-buster
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH = "${PATH}:/root/.poetry/bin"

RUN mkdir TO-DO-APP
COPY . ./TO-DO-APP

WORKDIR /TO-DO-APP
RUN poetry install
# ENTRYPOINT ["poetry run flask run"]
EXPOSE 5000
# ENTRYPOINT [ "poetry run gunicorn --bind 0.0.0.0:5000 wsgi:app" ]
ENTRYPOINT ["poetry", "run", "gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]


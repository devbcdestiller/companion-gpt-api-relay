FROM python:3.10.9

COPY . /flask_app
WORKDIR /flask_app

ENV PIPENV_VENV_IN_PROJECT=1

RUN set -ex && pip install -U pipenv
RUN set -ex && pipenv install --system

CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"]

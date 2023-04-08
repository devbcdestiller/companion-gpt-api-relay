FROM python:3.10.9

COPY . /sys-companion-gpt-api
WORKDIR /sys-companion-gpt-api

ENV PIPENV_VENV_IN_PROJECT=1

RUN set -ex && pip install -U pipenv
RUN set -ex && pipenv install --system

CMD ["gunicorn", "main:app", "--config", "gunicorn.conf.py"]

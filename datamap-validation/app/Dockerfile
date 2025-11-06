FROM python:trixie

WORKDIR /app

COPY . .

RUN python -m venv ./.venv
RUN . ./.venv/bin/activate
RUN pip install -r requirements.txt
FROM python:3.13.0

WORKDIR /usr/src/app
RUN python3.13 -m venv venv

COPY pyproject.toml /usr/src/app
ENV PATH="/usr/src/app/venv/bin:$PATH"
ENV PYTHONPATH="/usr/src/app"

RUN pip install --upgrade pip
RUN pip install fastapi psycopg2-binary sqlalchemy

RUN apt-get update
RUN apt-get install -qq -y apt-utils python3-dev libpq-dev
RUN pip install --upgrade uv
RUN uv pip install --no-cache-dir -r pyproject.toml
RUN apt-get purge -y --auto-remove libffi-dev libssl-dev
RUN rm -rf /usr/src/python ~/.cache
RUN rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
FROM python:3.11-slim

WORKDIR /app

COPY ./app /app/app
COPY ./requirements.txt /app/
COPY ./.env /app/.env

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

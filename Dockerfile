FROM python:3.9

WORKDIR /classforma

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app
COPY ./images ./images



CMD ["python", uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
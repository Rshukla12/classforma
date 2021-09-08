FROM python:3.9

RUN apt-get update
RUN apt-get -y install tesseract-ocr
ADD . /classforma
WORKDIR /classforma

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
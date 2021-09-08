# Classforma

This is an API for Optical Character Recoginiton with the help of FASTAPI and [Google's Tesseract OCR ](https://github.com/tesseract-ocr/tesseract).

## Screenshots:

![get_docs_list](https://github.com/Rshukla12/classforma/blob/master/Screenshots/get_docs_list.jpg)
![parse_sample_doc_1](https://github.com/Rshukla12/classforma/blob/master/Screenshots/parse_sample_doc_1.jpg)
![parse_sample_doc_2](https://github.com/Rshukla12/classforma/blob/master/Screenshots/parse_sample_doc_2.jpg)

## Endpoints:

### List endpoint:

url: http://localhost:5000/get_doc_list

output: list of document ids


### Parse endpoint: this endpoint extracts the text content the document (that matched <document_id>) of any of the documents passed in the url

url: http://localhost:5000/parse/sample_1.png

output: content of sample_1.png in text format

### Upload endpoint: this endpoints allows to upload images to be extracted ( Added Functionality )

url: POST http://localhost:5000/upload/

output: url to parse the uploaded image

## Deployments:

Install `git`,`python3`, `pip3`, `virtualenv` in your operating system

### Using Docker:

Install `docker` in your operating system

```
docker build -t imagename .                                           # Build the image
docker run run -d --name --name containername -p 5000:5000 imagename  # Build and run the container
```

### Without Docker:
Install [`Tesseract OCR`](https://tesseract-ocr.github.io/tessdoc/Downloads.html)
```
virtualenv -p python3 .venv		                              # Create virtualenv named .venv
source .venv/bin/activate		                              # Active virtualenv named .venv
pip install -r requirements.txt		                              # Install project requirements in .venv
uvicorn app.main:app --host 0.0.0.0 --port 5000                       # Run FAST API server
```

#### Errors

![#ff0000](https://via.placeholder.com/15/f03c15/000000?text=+) `tesseract not found/present` error arises check if the tesseract is set in the environment variable alternatively you can set path of the executable in the `OCR.py` file inside `app`.

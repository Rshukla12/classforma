from fastapi import FastAPI, UploadFile, File
from OCR import parse_text
import os
import shutil

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "list/": "List of the parable images",
        "parse/{image_name}/": "Parse the image named as image name"
    }


@app.get("/list/")
def parse_list():
    img_list = os.listdir("images")
    return {
        "Available Images": img_list,
        "To parse {image_name}": "http://localhost:5000/parse/{image_name}/"
    }


@app.get("/parse/{file_name}/")
async def parse_image(file_name: str):
    try:
        res = await parse_text(file_name)
    except Exception as E:
        res = f"Parsing wasn't done, a error occured :- {E}"
    return {
        "result": res
    }


@app.post("/upload/")
async def upload(image: UploadFile = File(...)):
    path = f"./images/{image.filename}"
    with open(path, "wb+") as file_object:
        shutil.copyfileobj(image.file, file_object)
    return {"to_parse": f"http://localhost:5000/parse/{image.filename}"}

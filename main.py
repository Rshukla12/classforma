from fastapi import FastAPI
from OCR import parse_text
import os

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
    except:
        res = "Parsing wasn't done, Please see the url"
    return {
        "result": res
    }

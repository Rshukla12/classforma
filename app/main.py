from fastapi import FastAPI, UploadFile, File
from app.OCR import parse_text
import os
import shutil

app = FastAPI()


@app.get("/")
def read_root():
    """
    Home/Base url
    :return: response with the available urls and their description
    """
    return {
        "/get_doc_list/": "List of the parable images",
        "/parse/{image_name}/": "Parse the image named as image name",
        "/upload/": "To upload an image"
    }


@app.get("/get_doc_list/")
def parse_list():
    """
    The available images
    :return: response of the available docs to be parsed
    """
    img_list = os.listdir("../images")
    return {
        "Available Images": img_list,
        "To parse {image_name}": "http://localhost:5000/parse/{image_name}/"
    }


@app.get("/parse/{file_name}/")
async def parse_image(file_name: str):
    """
    Parses text from the image by calling OCR function
    :param file_name: name of the file to parsed
    :return: response containing the parsed text
    """
    try:
        res = await parse_text(file_name)
    except Exception as E:
        res = f"an error occurred while parsing, detail of error is as follows\n {E}"
    return {
        "result": res
    }


@app.post("/upload/")
async def upload(image: UploadFile = File(...)):
    """
    Upload images to the server
    :param image: file to be uploaded
    :return: response containing  url to parse text from image or error
    """
    try:
        path = f"../images/{image.filename}"
        with open(path, "wb+") as file_object:
            shutil.copyfileobj(image.file, file_object)
        return {"to_parse": f"http://localhost:5000/parse/{image.filename}"}
    except Exception as E:
        err = f"an error occurred while uploading, detail of error is as follows\n {E}"
        return {
            "error": err
        }

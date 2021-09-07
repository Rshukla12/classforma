from PIL import Image
import pytesseract

# To use Tesseract pytesseract needs the Tesseract executable
# Change it to wherever the tesseract executable is install
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


async def parse_text(filename: str):
    """
    Parse text from the given filename
    :param filename: name of the file to extract the data
    :return: text extracted from the file
    """
    text = pytesseract.image_to_string(Image.open(f"app/images/{filename}"))
    return text



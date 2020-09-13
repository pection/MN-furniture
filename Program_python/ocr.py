try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import argparse

parser = argparse.ArgumentParser(description='This is Resize image  script')
parser.add_argument('-i','--in',action='store',dest='input',default=None,help='<Required>image path',required=True)
results = parser.parse_args()
imgpath = results.input
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename),lang='tha')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
pytesseract.pytesseract.tesseract_cmd =  '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
file1 = open("../static/txt/Address.txt","w") 
# L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
  
# \n is placed to indicate EOL (End of Line) 
file1.write(ocr_core(imgpath))
file1.close() #to change file access modes 

# print(ocr_core(imgpath))
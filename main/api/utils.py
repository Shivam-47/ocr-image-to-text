from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import boto3
import botocore
from .constants import bucket_name, save_folder
import os

def download_image(key):
    _bucket_name = bucket_name 
    _key = key 
    s3 = boto3.resource('s3')

    try:
        s3.Bucket(_bucket_name).download_file(_key, save_folder+"/"+_key)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    fname= save_folder+"/"+_key

    return fname

def delete_file(fname):
    try:
        os.remove(fname)
        print("Deleted successfuly")
    except Exception as error:
        print(error)
    

def image_to_text_ocr(key):

    fname = download_image(key)
   
    text = str(((pytesseract.image_to_string(Image.open(fname)))))
    text = text.replace('-\n','')
    text = text.replace('\n','')
    text = text.replace('','')

    delete_file(fname)

    return text
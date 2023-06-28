from .models import Data
import uuid

def save_data(text,id):
    data = Data()
    data.session_id = uuid.uuid1()
    data.ocr_text = text
    data.src_image =  id
    data.save()
from django.db import models
import time

class Data(models.Model):
    session_id = models.CharField(max_length=50,db_index=True)
    src_image = models.CharField(max_length=100)
    ocr_text = models.TextField()
    
    
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from .utils import image_to_text_ocr
from .manager import save_data

def ocr_api(req,id):
    result =image_to_text_ocr(id)
    save_data(result,id)    
    return JsonResponse({'result': result} )
    # return render(req,'api/index.html',{'text':result})
    







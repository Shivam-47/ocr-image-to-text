from django.http import HttpResponse
from django.shortcuts import render
import environ 

env = environ.Env(
    DEBUG=(bool,False)
)
# reading .env file
environ.Env.read_env()


def home_page(req):
    return render(req,'index.html',{'lambda_api': env.str('API_CALL')})






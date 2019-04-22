from django.shortcuts import render
#不用摸板
# Create your views here.
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseBadRequest
import simplejson
from .models import User
import logging
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

def checkemail(request):#判断email
    return HttpResponse()

def reg(request:HttpRequest):
    print(request, '-------------')
    try:
        print(request.body)
        payload = simplejson.loads(request.body)
        print(payload)
        email = payload['email']
        #数据库中看看email有没有
        mgr = User.objects.filter(email=email)
        print(mgr)
        print(type(mgr))
        if mgr:
            return HttpResponseBadRequest()

        name = payload['name']
        password = payload['password']
        user = User()
        user.name = name
        user.password = password
        user.email = email
        user.save()
        return HttpResponse({"user":user.id})

    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()


    
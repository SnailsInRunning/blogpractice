"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include

# from django.http import HttpResponse , JsonResponse
# from django.template.loader import get_template
# #模板
# from django.shortcuts import render

# from user.views import reg


# post={'user':'hello world','name':'海州','sex':'male'}


# def index(request):
#     print(request)
#     print(type(request))

#     return render(request, 'index.html', {'post':post})
#     #return JsonResponse({'user':'hello world'})

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index$',index),
    # url(r'^$', index),
    url(r'^user/', include('user.urls'))
]

from django.shortcuts import render
from django.http import HttpResponse
from .forms import URLform

import secrets

def home(request):
    return HttpResponse('Hello.')

def shorten(request):
    if request.method == "POST":
        userform = URLform(request.POST)
        longurl = userform.data['longurl']
        shorturl = secrets.token_hex(4)
        return HttpResponse(shorturl)
    else:
         myform = URLform()
         return render(request,'form.html',{'form':myform})

def redirect_url(request,link):
    # from <slug:link>
    # slug is datatype
    return HttpResponse(link)


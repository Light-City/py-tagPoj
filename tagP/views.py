from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def query(request):
    l=["存","正","参"]
    l=[]
    d={'name':'见','age':12,'sex':'M'}
    return render(request,'index.html',locals())

def login(req):
    return HttpResponse('ok')
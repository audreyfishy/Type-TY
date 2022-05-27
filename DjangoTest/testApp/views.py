from django.shortcuts import render
from django.http import HttpResponse
from testApp.functions import functions as f

def index(request):
    return render(request, 'index.html')

def form(request):
    print("saki")
    f.main("UCl79rcNN4Nxps7I0d-iXJpQ")
    print("ato")
    return HttpResponse()

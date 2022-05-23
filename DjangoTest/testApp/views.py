from django.shortcuts import render

# Create your views here.
def index(request):
    print("indeisa")
    return render(request, 'index.ejs')
from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'intro/base.html',{"message":"hey im in"})

def index(request):
    return render(request,'intro/index.html')
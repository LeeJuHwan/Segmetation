from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
def index(request) :
    return render(request, "body.html")

def error_404_view(request, exception) :
    return render(request, "404.html")

def error_500_view(request) : 
    return render(request, "500.html")

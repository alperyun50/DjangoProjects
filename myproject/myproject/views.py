# from django.http import HttpResponse
from django.shortcuts import render

# def homepage(request):
#     return HttpResponse("hello world! I'm home. ")
def homepage(request):
    return render(request, 'home.html')

# def about(request):
#     return HttpResponse("my about page")
def about(request):
    return render(request, 'about.html')
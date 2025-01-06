from django.http import HttpResponse

def homepage(request):
    return HttpResponse("hello world! I'm home. ")

def about(request):
    return HttpResponse("my about page")
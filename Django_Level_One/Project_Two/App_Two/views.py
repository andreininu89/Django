from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<em> My Second App </em>")


def help_me(request):
    help_dict = {"help_insert": "Hello World! THIS IS THE HELP PAGE"}
    return render(request, "App_Two/help.html", context=help_dict)

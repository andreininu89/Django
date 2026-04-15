from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


# Create your views here.
class CBView(View):
    def get(self, request):
        return HttpResponse("Hello World! This is a Class Based View")


class IndexView(TemplateView):
    template_name = "index.html"

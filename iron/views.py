from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest

# Create your views here.


class Iron(TemplateView):
    template_name = 'index.html'
    print()

class Man(TemplateView):
    template_name = 'index2.html'

class Real(TemplateView):
    template_name = 'index3.html'



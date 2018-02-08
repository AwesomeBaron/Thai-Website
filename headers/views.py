from django.shortcuts import render, get_object_or_404
from django.template import loader


def index(request):
    template = 'headers/index.html'
    context = {}
    return render(request, template, context)


def about(request):
    template = 'headers/About.html'
    context = {}
    return render(request, template, context)


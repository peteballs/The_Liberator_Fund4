from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def ai_description(request):
    return render(request, 'pages/ai_description.html')

def disclaimer(request):
    return render(request, 'pages/disclaimer.html')

def results(request):
    return render(request, 'pages/results.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view that displays the landing page"""
    return render(request, 'index.html')

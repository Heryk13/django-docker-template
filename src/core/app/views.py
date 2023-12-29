from django.shortcuts import render
from .dash_app.main import app

# Create your views here.
def index(request):
    return render(request, 'index.html')
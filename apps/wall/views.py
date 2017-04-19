from django.shortcuts import render
from .models import User, Message, Comment

def index(request):
    return render(request, "index/index.html")
# Create your views here.

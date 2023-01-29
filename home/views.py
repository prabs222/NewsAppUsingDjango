from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html' , context={"articles": Article.objects.all().order_by('-created_at')})
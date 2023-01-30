from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    context = {}
    articles_obj = Article.objects.all()
    page = request.GET.get('page', 1)
    p = Paginator(articles_obj,15)
    try:
        articles_obj = p.page(page)
    except :
        articles_obj = p.page(1)
    return render(request, 'home.html' , context={"articles": articles_obj})
        
    
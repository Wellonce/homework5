from django.shortcuts import render
from .models import New

# Create your views here.
def home_page(request):
    news = New.objects.all()
    context = {
        "news": news
    } 
    return render (request, 'index.html', context= context)

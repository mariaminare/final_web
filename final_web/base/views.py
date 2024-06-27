from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

# Create your views here.
def home(request):
    players=Player.objects.all()
    context= {"players":players}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')
def contact(request):
    return render(request, 'base/contact.html')
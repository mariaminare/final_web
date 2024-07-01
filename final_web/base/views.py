from django.shortcuts import render
from django.http import HttpResponse
from .models import Player,User

# Create your views here.
def home(request):
    players=Player.objects.all()
    context= {"players":players}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def profile(request, pk):
    user= User.objects.get(id=int(pk))
    players= user.players.all()
    context={"players":players, "user":user}
    return render(request, 'base/profile.html',context)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player,User,Club
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    p=request.GET.get("p") if request.GET.get('p') != None else ""
    #players=Player.objects.all()
    players= Player.objects.filter(Q(first_name__icontains=p) | Q(last_name__icontains=p) |Q(nationality__name__icontains=p)| Q(current_club__name__icontains=p) )
    #players=list(set(players)) ar mchirdeba, ertze met clubsa da erovnul gundshi ver iqnebian
    clubs=Club.objects.all()
    heading="Famous Players:"
    context= {"players":players, "heading":heading, "clubs":clubs}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def profile(request, pk):
    user= User.objects.get(id=int(pk))
    p = request.GET.get("p") if request.GET.get('p') != None else ""
    # players=user.objects.all()
    players = user.players.filter(Q(first_name__icontains=p) | Q(last_name__icontains=p) | Q(nationality__name__icontains=p) | Q(current_club__name__icontains=p))
    # players=list(set(players)) ar mchirdeba, ertze met clubsa da erovnul gundshi ver iqnebian
    clubs = Club.objects.all()
    heading="My Favourite Players:"
    context={"players":players, "user":user, "heading":heading, "clubs":clubs}
    return render(request, 'base/profile.html',context)


def adding(request, id):
    player=Player.objects.get(player_id=id)
    user= request.user
    user.players.add(player)
    return redirect('profile', user.id)

def delete(request, id):
    player =Player.objects.get(player_id=id)

    if request.method == "POST":
        request.user.players.remove(player)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'player': player})


def login_page(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username= request.POST.get('username').lower()
        password= request.POST.get('password').lower()

        try:
            user= User.objects.get(username=username)
        except:
            pass #Error Message
        user=  authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            pass  #Error Message


    context={'page': page}
    return render(request, 'base/login_register.html', context)

def logout_page(request):
    logout(request)
    return redirect('home')

def register_page(request):
    context={}
    return render(request, 'base/login_register.html', context)


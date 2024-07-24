from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player,User,Club, Nation
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, PlayerForm, UserForm, CommentForm
from .seeder import seeder_func
from django.contrib import messages


# Create your views here.
def home(request):
    p=request.GET.get("p") if request.GET.get('p') != None else ""
    # seeder_func()
    #players=Player.objects.all()
    players= Player.objects.filter(Q(first_name__icontains=p) | Q(last_name__icontains=p) |Q(nation__name__icontains=p)| Q(club__name__icontains=p) )
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
    players = user.players.filter(Q(first_name__icontains=p) | Q(last_name__icontains=p) | Q(nation__name__icontains=p) | Q(club__name__icontains=p))
    # players=list(set(players)) ar mchirdeba, ertze met clubsa da erovnul gundshi ver iqnebian
    clubs = Club.objects.all()
    heading="My Favourite Players:"
    context={"players":players, "user":user, "heading":heading, "clubs":clubs}
    return render(request, 'base/profile.html',context)

@login_required(login_url='login')
def adding(request, id):
    player=Player.objects.get(player_id=id)
    user= request.user
    user.players.add(player)
    return redirect('profile', user.id)

@login_required(login_url='login')
def delete(request, id):
    player =Player.objects.get(player_id=id)

    if request.method == "POST":
        request.user.players.remove(player)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'player': player})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username= request.POST.get('username').lower()
        password= request.POST.get('password').lower()

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,"Username doesn't exist!")
        user=  authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or password is incorrect!")
    return render(request, 'base/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form=MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    context={'form':form}
    return render(request, 'base/register.html', context)


def add_player(request):
    nations= Nation.objects.all()
    clubs=Club.objects.all()
    form=PlayerForm()

    if request.method == "POST":
        player_nation= request.POST.get("nation")
        player_club=request.POST.get("club")

        nation, created= Nation.objects.get_or_create(name=player_nation)
        club, created= Club.objects.get_or_create(name=player_club)

        form=PlayerForm(request.POST)

        new_player=Player(
            picture=request.FILES['picture'],
            first_name=form.data['first_name'],
            last_name=form.data['last_name'],
            date_of_birth=form.data['date_of_birth'],
            nation=nation,
            position=form.data['position'],
            previous_clubs=form.data['previous_clubs'],
            international_caps=form.data['international_caps'],
            goals_scored=form.data['goals_scored'],
            height=form.data['height'],
            weight=form.data['weight'],
            preferred_foot=form.data['preferred_foot'],
            biography=form.data['biography'],
            achievements=form.data['achievements'],
            club=club,
            creator=request.user
        )

        if not (Player.objects.filter(first_name=new_player.first_name) and Player.objects.filter(last_name=new_player.last_name) and Player.objects.filter(date_of_birth=new_player.date_of_birth)):
            new_player.save()
            # new_player.club.add(club)
            return redirect('home')


        return redirect('home')

    context= {'form':form,'nations':nations, 'clubs':clubs}
    return render(request, 'base/add_player.html',context)


def delete_player(request,id):
    player=Player.objects.get(player_id=id)
    if request.method == 'POST':
        player.picture.delete #static/files aqedanac shlis suratebs
        player.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'player': player})


@login_required(login_url='login')
def update_user(request):
    user= request.user
    form= UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id )
    return render(request, 'base/update_user.html',{'form':form})
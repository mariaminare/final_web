from django.shortcuts import render
from django.http import HttpResponse
from .models import Player,User,Club
from django.db.models import Q
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


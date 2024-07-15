from .models import Nation,Club

def seeder_func():
    nations= ['USA', 'Spain', 'Sweden', 'England', 'Georgia', ]
    clubs= ['Arsenal', 'Manchester City', 'Manchester United', 'Barcelona',]

    for nation in nations:
        if not Nation.objects.filter(name=nation):
            new_nation=Nation(name=nation)
            new_nation.save()

    for club in clubs:
        if not Club.objects.filter(name=club):
            new_club=Club(name=club)
            new_club.save()

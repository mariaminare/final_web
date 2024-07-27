from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Player
from .serializers import PlayerSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET api/",
        "GET api/books",
        "GET api/books/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def get_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_player(request,id):
    player = Player.objects.get(player_id=id)
    serializer = PlayerSerializer(player, many=False)
    return Response(serializer.data)






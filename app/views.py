from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Player
from app.src.update_db import update_all


def index(request):
    return render(request, 'index.html')


def search(request):
    name = request.GET.get('name')
    bnet_id = request.GET.get('bnet_id')
    try:
        limit = int(request.GET.get('limit', 25))
    except ValueError:
        limit = 25
    limit = min(limit, 200)
    if bnet_id is not None:
        players = Player.players.filter(bnet_id__iexact=f'{name}#{bnet_id}').order_by('-mmr')[:limit]
    else:
        bnet_or_name_filter = Q(bnet_id__istartswith=name) | Q(username__istartswith=name)
        players = Player.players.filter(bnet_or_name_filter).order_by('-mmr')[:limit]
    pages_required = (len(players) > 0) - 1
    return render(request, 'search.html', {
        'players': players,
        'page_number': 0,
        'pages_required': pages_required
    })


def ladder(request):
    return render(request, 'search.html')


def about(request):
    return render(request, 'about.html')


def update_db(request):
    update_all()
    return HttpResponse('done')

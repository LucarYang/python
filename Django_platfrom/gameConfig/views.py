from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import gameinfo
from CommonApps.views import log_in

# Create your views here.
@log_in
def gameList(request):
    if request.method == 'GET':
        gameList = gameinfo.objects.filter()
        return  render(request, 'gameConfig/gameList.html',{'gameList':gameList})


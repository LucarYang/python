from django.shortcuts import render

# Create your views here.
def gameList(request):
    return  render(request, 'gameConfig/gameList.html')


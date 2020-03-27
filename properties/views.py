from django.shortcuts import render
from django.http import HttpResponse


def display(request):
    return render(request, 'properties/display.html')


def start_game(request):
    return render(request, 'properties/start_game.html')

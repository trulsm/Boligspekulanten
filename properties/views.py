from django.shortcuts import render
from django.http import HttpResponse

from .models import Property
import random


def display(request):
    properties = Property.objects.all()
    random_property = random.choice(properties)

    context = {
        'property': random_property
    }
    return render(request, 'properties/display.html', context)


def start_game(request):
    return render(request, 'properties/start_game.html')

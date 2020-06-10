from django.shortcuts import render
from django.http import HttpResponse

from .models import Property
import random


def display(request):
    properties = Property.objects.all()

    if 'omrade1' in request.POST:
        omrade1 = request.POST['omrade1']
        if omrade1:
            properties = properties.filter(omrade1__icontains=omrade1)
    if 'omrade2' in request.POST:
        omrade2 = request.POST['omrade2']
        if omrade2:
            properties = properties.filter(omrade2__icontains=omrade2)

    random_property = random.choice(properties)

    mapstring = "+".join(",".join("Benneches gate 6, 0169 Oslo".split(", ")).split())

    context = {
        'property': random_property,
        'omrade1': omrade1,
        'omrade2': omrade2,
        'mapstring': mapstring
    }
    return render(request, 'properties/display.html', context)


def start_game(request):
    return render(request, 'properties/start_game.html')


def choose_area(request):

    properties = Property.objects.order_by('-id')

    if 'omrade1' in request.GET:
        omrade1 = request.GET['omrade1']
        if omrade1:
            properties = properties.filter(omrade1__icontains=omrade1)
    if 'omrade2' in request.GET:
        omrade2 = request.GET['omrade2']
        if omrade2:
            properties = properties.filter(omrade2__icontains=omrade2)

    random_property_in_selected_area = random.choice(properties)
    context = {
        'omrade1': omrade1,
        'omrade2': omrade2,
        'property': random_property_in_selected_area
    }
    return render(request, 'properties/display.html', context)

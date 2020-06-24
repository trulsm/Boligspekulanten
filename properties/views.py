from django.shortcuts import render
from django.http import HttpResponse

from .models import Property
import random


def display(request):
    properties = Property.objects.all()

    if 'area1' in request.POST:
        area1 = request.POST['area1']
        if area1:
            properties = properties.filter(area1__icontains=area1)
    if 'area2' in request.POST:
        area2 = request.POST['area2']
        if area2:
            properties = properties.filter(area2__icontains=area2)

    random_property = random.choice(properties)

    mapstring = "+".join(",".join("Benneches gate 6, 0169 Oslo".split(", ")).split())

    context = {
        'property': random_property,
        'area1': area1,
        'area2': area2,
        'mapstring': mapstring
    }
    return render(request, 'properties/display.html', context)


def start_game(request):
    return render(request, 'properties/start_game.html')


def choose_area(request):

    properties = Property.objects.order_by('-id')

    if 'area1' in request.GET:
        area1 = request.GET['area1']
        if area1:
            properties = properties.filter(area1__icontains=area1)
    if 'area2' in request.GET:
        area2 = request.GET['area2']
        if area2:
            properties = properties.filter(area2__icontains=area2)

    random_property_in_selected_area = random.choice(properties)
    context = {
        'area1': area1,
        'area2': area2,
        'property': random_property_in_selected_area
    }
    return render(request, 'properties/display.html', context)

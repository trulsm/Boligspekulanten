from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Prediction
from .models import Property
import random


def prediction(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        property_adresse = request.POST['property_adresse']
        user_id = request.POST['user_id']
        user_username = request.POST['user_username']
        price_prediction = request.POST['price_prediction']
        #prediction_date = request.POST['prediction_date']

        prediction = Prediction(property_id=property_id, property_adresse=property_adresse, user_id=user_id, user_username=user_username, price_prediction=price_prediction)

        prediction.save()

        messages.success(
            request, 'Your prediction have been submitted. Here is a new challenge.')

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
    mapstring = "+".join(",".join(random_property.adresse.split(", ")).split())
    context = {
        'omrade1': omrade1,
        'omrade2': omrade2,
        'property': random_property,
        'mapstring': mapstring
    }

    return render(request, 'properties/display.html', context)

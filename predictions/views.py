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

        prediction = Prediction(property_id=property_id, property_address=property_adresse, user_id=user_id, user_username=user_username, price_prediction=price_prediction)

        prediction.save()

        messages.success(
            request, 'Your prediction have been submitted. Here is a new challenge.')

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
    mapstring = "+".join(",".join(random_property.address.split(", ")).split())
    context = {
        'area1': area1,
        'area2': area2,
        'property': random_property,
        'mapstring': mapstring
    }

    return render(request, 'properties/display.html', context)

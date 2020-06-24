from django.db import models
from datetime import datetime
from properties.models import Property
from django.contrib.auth.models import User

class Prediction(models.Model):
    property_id = models.IntegerField()
    property_address = models.CharField(max_length=200, null=True, blank=True)
    user_id = models.IntegerField()
    user_username = models.CharField(max_length=200, null=True, blank=True)
    price_prediction = models.FloatField(null=True)
    actual_price = models.FloatField(null=True, blank=True)
    prediction_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.property_address


    ## OBS: __str__ funksjonen het før __int__ av en eller annen grunn. Visste ikke hvorfor og endret den til __str__ som i de andre modellene.

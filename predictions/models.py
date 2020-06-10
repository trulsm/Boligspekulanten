from django.db import models
from datetime import datetime
from properties.models import Property
from django.contrib.auth.models import User

class Prediction(models.Model):
    #property_id = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    property_id = models.IntegerField()
    property_adresse = models.CharField(max_length=200, null=True, blank=True)
    #user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user_id = models.IntegerField()
    user_username = models.CharField(max_length=200, null=True, blank=True)
    price_prediction = models.IntegerField()
    actual_price = models.IntegerField(null=True, blank=True)
    prediction_date = models.DateTimeField(default=datetime.now, blank=True)
    def __int__(self):
        return self.id

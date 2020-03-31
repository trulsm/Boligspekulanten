from django.db import models
from properties.models import Property
from django.contrib.auth.models import User


class Prediction(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    price_prediction = models.IntegerField()
    actual_price = models.IntegerField()
    def __int__(self):
        return self.property_id



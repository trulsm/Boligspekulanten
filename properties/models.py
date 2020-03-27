from django.db import models

class Property(models.Model):
    adresse = models.CharField(max_length=200)
    finnkode = models.IntegerField()
    link = models.CharField(max_length=200)
    pris = models.IntegerField()
    totalpris = models.IntegerField()
    areal = models.IntegerField()
    megler = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    actual_price = models.IntegerField(default=0)
    def __str__(self):
        return self.adresse

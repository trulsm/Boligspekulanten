from django.db import models

class Property(models.Model):
    finnkode = models.IntegerField()
    link = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    omrade1 = models.CharField(max_length=100)
    omrade2 = models.CharField(max_length=100)
    pris = models.IntegerField()
    fellesgjeld = models.IntegerField()
    fellesformue = models.IntegerField()
    omkostninger = models.IntegerField()
    totalpris = models.IntegerField()
    felleskost = models.IntegerField()
    areal = models.IntegerField()
    etasje = models.IntegerField()
    byggear = models.IntegerField()
    megler = models.CharField(max_length=200)
    sold = models.BooleanField(default=False)
    actual_price = models.IntegerField(default=0)
    def __str__(self):
        return self.adresse

# Generated by Django 3.0.4 on 2020-04-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_auto_20200419_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='BRLandel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='BRLnavn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='BRLorgnr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='beskrivelse',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bolignummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='boligtype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bruksareal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='bruttoareal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='eierform',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='eierskifteforsikring',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='energimerking',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='formuesverdi',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='gardsnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='kommunenummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='referansenummer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='seksjonsnummer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='siste_endring',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='tomteareal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

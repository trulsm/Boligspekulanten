# Generated by Django 3.0.4 on 2020-04-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_auto_20200420_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='BRLandel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bolignummer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='byggear',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='etasje',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='gardsnummer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='kommunenummer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='seksjonsnummer',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

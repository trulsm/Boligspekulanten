# Generated by Django 3.0.4 on 2020-05-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_auto_20200421_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='forste_visning',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='siste_visning',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

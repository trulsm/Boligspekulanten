# Generated by Django 3.0.4 on 2020-04-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_property_omrade1'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='omrade2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
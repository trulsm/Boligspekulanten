# Generated by Django 3.0.4 on 2020-04-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20200420_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='beskrivelse',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]

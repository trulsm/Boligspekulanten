# Generated by Django 3.0.4 on 2020-04-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0003_auto_20200421_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='actual_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
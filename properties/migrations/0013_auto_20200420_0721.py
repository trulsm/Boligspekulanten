# Generated by Django 3.0.4 on 2020-04-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_auto_20200419_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bruksareal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bruttoareal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='fellesformue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='fellesgjeld',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='felleskostnader',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='formuesverdi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='omkostninger',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='primarareal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='prisantydning',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='salgspris',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='tomteareal',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='totalkostnad',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

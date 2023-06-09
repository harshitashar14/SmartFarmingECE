# Generated by Django 4.2 on 2023-04-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusitem',
            name='Crop_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='statusitem',
            name='Is_sprinkler_on',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='statusitem',
            name='Moisture',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='statusitem',
            name='Optimal_humidity',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='statusitem',
            name='Optimal_moisture',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='statusitem',
            name='Optimal_temp',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='statusitem',
            name='Humidity',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='statusitem',
            name='Temp',
            field=models.FloatField(default=1),
        ),
    ]

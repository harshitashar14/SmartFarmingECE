# Generated by Django 4.2 on 2023-04-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateField(auto_now=True)),
                ('Temp', models.FloatField()),
                ('Humidity', models.FloatField()),
            ],
        ),
    ]
# Generated by Django 4.0 on 2022-02-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supergame', '0011_jugadores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ganadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
            ],
        ),
    ]
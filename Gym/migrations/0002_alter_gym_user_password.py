# Generated by Django 4.2.6 on 2024-01-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym_user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]

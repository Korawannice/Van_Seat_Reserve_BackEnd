# Generated by Django 5.0.3 on 2024-03-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('van_re', '0004_alter_customuser_managers_alter_carreservation_car_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreservation',
            name='number_of_ticket',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('van_re', '0002_cardriver_endroute_cardriver_is_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
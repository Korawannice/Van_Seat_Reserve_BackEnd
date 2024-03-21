from django.db import models 
from django.contrib.auth.models import AbstractUser
import random
import string


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('driver', 'Driver'),
    )
    
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
        validators=[AbstractUser.username_validator],
    )
    role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    prefix = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.username

## --- van_reservation ---

class Locations(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class VanDriver(models.Model):
    

    van_number = models.CharField(max_length=50)
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number_of_seat = models.IntegerField(default=12)
    price_per_unit = models.FloatField()
    is_available = models.BooleanField(default=True)
    startRoute = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='start_route')
    endRoute = models.ForeignKey(Locations, on_delete=models.CASCADE, related_name='end_route')
    date = models.DateField()
    time = models.TimeField()
    
    
    def __str__(self):
        return self.van_number

class VanReservation(models.Model):
    number_of_ticket = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='user')
    van = models.ForeignKey(VanDriver, on_delete=models.CASCADE, related_name='van')
    number_of_seat = models.IntegerField()
    amount_to_pay = models.FloatField()
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.number_of_ticket:
            self.number_of_ticket = self.generate_number_of_ticket()
        super().save(*args, **kwargs)

    def generate_number_of_ticket(self):
        number_of_ticket = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        while VanReservation.objects.filter(number_of_ticket=number_of_ticket).exists():
            number_of_ticket = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return number_of_ticket


# class Payment(models.Model):
#     reservation = models.ForeignKey(VanReservation, on_delete=models.CASCADE , related_name='reservation')
#     amount = models.FloatField()
#     is_paid = models.BooleanField(default=False)

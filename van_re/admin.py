from django.contrib import admin
from .models import CustomUser , CarDriver , CarReservation , Locations

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CarDriver)
admin.site.register(CarReservation)
# admin.site.register(Payment)
admin.site.register(Locations)




from django.contrib import admin
from .models import CustomUser , VanDriver , VanReservation , Locations

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(VanDriver)
admin.site.register(VanReservation)
# admin.site.register(Payment)
admin.site.register(Locations)

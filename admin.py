from django.contrib import admin

# Register your models here.
from .models import Movie, Guest, Reservation

admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(Reservation)
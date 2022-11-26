from django.db import models

#movie
class Movie(models.Model):
    hall = models.CharField(max_length=15)
    movie = models.CharField(max_length=15)
    date = models.DateField()
#guest

class Guest(models.Model):
    name = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)


#reservations
class Reservation(models.Model):
    guest = models.ForeignKey(Guest, related_name='reservation', on_delete=models.CASCADE )
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE )
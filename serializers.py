from rest_framework import serializers
from tickets.models import Guest,Movie,Reservation

#movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
#guest
class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ['pk', 'reservation', 'name', 'mobile']
#reservations
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
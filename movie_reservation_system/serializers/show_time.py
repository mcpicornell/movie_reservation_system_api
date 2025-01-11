from rest_framework import serializers
from movie_reservation_system.models import ShowTime


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        exclude = ['created_at']
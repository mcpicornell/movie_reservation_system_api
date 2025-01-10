from rest_framework import serializers
from movie_reservation_system.models import Seat, Room, Row

class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['name']

class SeatSerializer(serializers.ModelSerializer):
    row = serializers.CharField(source='row.name', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Seat
        fields = ['name', 'row', 'room']

class RoomSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['name',  'seats']
from rest_framework import serializers
from movie_reservation_system.models import Seat, Room, Row

class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['name']

class SeatSerializer(serializers.ModelSerializer):
    row = serializers.CharField(source='row.name', read_only=True)
    room = serializers.CharField(source='room.name', read_only=True)
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ['name', 'row', 'room']

    def get_is_available(self, obj):
        show_time_id = self.context.get('show_time_id')
        show_time_day = self.context.get('show_time_day')

        if show_time_id is None or show_time_day is None:
            return False

        return obj.is_available(show_time_id=show_time_id, show_time_day=show_time_day)

class RoomSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['name',  'seats']
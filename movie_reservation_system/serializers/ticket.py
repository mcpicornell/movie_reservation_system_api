from rest_framework import serializers
from movie_reservation_system.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    display_name = serializers.SerializerMethodField()
    start_show_time = serializers.CharField(source='show_time.start_show_time', read_only=True)


    class Meta:
        model = Ticket
        fields = ['id', 'user', 'start_show_time', 'display_name', 'show_time_day']

    @staticmethod
    def get_display_name(obj):
        return obj.get_display_name()
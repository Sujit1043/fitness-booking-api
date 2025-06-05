from rest_framework import serializers
from .models import FitnessClass, Booking
from pytz import timezone

class FitnessClassSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'datetime', 'instructor', 'available_slots']

    def get_datetime(self, obj):
        tz = self.context.get('timezone', 'Asia/Kolkata')
        return obj.datetime_ist.astimezone(timezone(tz)).isoformat()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

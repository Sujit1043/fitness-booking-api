from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils import timezone
from django.shortcuts import get_object_or_404

class FitnessClassList(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(datetime_ist__gte=timezone.now())
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)
    


class BookClass(APIView):
    def post(self, request):
        data = request.data
        required_fields = ['class_id', 'client_name', 'client_email']
        for field in required_fields:
            if field not in data:
                return Response({'error': f'{field} is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            fitness_class = FitnessClass.objects.get(id=data['class_id'])
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Class not found.'}, status=status.HTTP_404_NOT_FOUND)

        if fitness_class.available_slots <= 0:
            return Response({'error': 'No slots available.'}, status=status.HTTP_400_BAD_REQUEST)

        Booking.objects.create(
            fitness_class=fitness_class,
            client_name=data['client_name'],
            client_email=data['client_email']
        )
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response({'message': 'Booking successful!'}, status=status.HTTP_201_CREATED)


class GetBookings(APIView):
    def get(self, request):
        email = request.GET.get('client_email')
        if not email:
            return Response({'error': 'client_email is required as query param'}, status=status.HTTP_400_BAD_REQUEST)
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

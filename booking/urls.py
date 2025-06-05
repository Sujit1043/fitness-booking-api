from django.urls import path
from .views import FitnessClassList, BookClass, GetBookings


urlpatterns = [
    # path('classes/', FitnessClassList.as_view()),
    path('classes/', FitnessClassList.as_view(), name='class-list'),
    path('book/', BookClass.as_view()),
    path('bookings/', GetBookings.as_view()),
]

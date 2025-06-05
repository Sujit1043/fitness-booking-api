import os
import django
from datetime import datetime
import pytz

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_booking.settings')
django.setup()

from booking.models import FitnessClass

def seed():
    ist = pytz.timezone('Asia/Kolkata')
    classes = [
        {"name": "Yoga", "datetime_ist": ist.localize(datetime(2025, 6, 5, 8)), "instructor": "Alice", "available_slots": 5},
        {"name": "Zumba", "datetime_ist": ist.localize(datetime(2025, 6, 5, 10)), "instructor": "Bob", "available_slots": 8},
        {"name": "HIIT", "datetime_ist": ist.localize(datetime(2025, 6, 5, 18)), "instructor": "Charlie", "available_slots": 10}
    ]

    for c in classes:
        FitnessClass.objects.create(**c)

if __name__ == "__main__":
    seed()

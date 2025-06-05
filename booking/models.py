from django.db import models

# Create your models here.
class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    datetime_ist = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.IntegerField()

    def __str__(self):
        return f"{self.name} by {self.instructor}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"

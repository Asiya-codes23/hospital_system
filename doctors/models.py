from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    availability = models.CharField(max_length=50, choices=[
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
        ('On Leave', 'On Leave'),
    ])
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.full_name} ({self.specialization})"


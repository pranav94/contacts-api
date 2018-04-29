from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    work_phone = models.CharField(max_length=15)
    cell_phone = models.CharField(max_length=15)
    lattitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

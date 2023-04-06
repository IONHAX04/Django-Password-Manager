from django.db import models

# Create your models here.

class Manage(models.Model):
    domains = models.CharField(max_length=100)
    emails = models.CharField(max_length=100)
    passwords = models.CharField(max_length=100)
    mobile_numbers = models.CharField(max_length=10)

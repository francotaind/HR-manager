from django.db import models
from datetime import date

class Employee(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('STAFF', 'Staff'),
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateField()
    contract_length = models.IntegerField(help_text="Contract length in months")
    contract_end = models.DateField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    @property
    def days_until_contract_end(self):
        return (self.contract_end - date.today()).days

    def __str__(self):
        return self.name

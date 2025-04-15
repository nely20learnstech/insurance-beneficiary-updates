from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# User parent class
class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
    
class Employee(User):
    employee_id = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    insurance_policy_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
    

class Insurance(models.Model):
    provider_name = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=20, unique=True)
    coverage_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.provider_name
    
class HR(Employee):
    hr_id = models.CharField(max_length=10, unique=True)
    is_advisor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class user(AbstractUser):
    pass
class Speciality(models.Model):
    name =models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)
    
class Doctor(User):

    license_number=models.CharField(max_length=6 , unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone =models.CharField(max_length=8)
    created_at =models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)
   # specialtie=models.ManyToManyField("AccountApp.Specialtie")
    specialties=models.ManyToManyField(Speciality , related_name="doctors")
    
NumberValidator=RegexValidator(
    regex=r'^\d{8}$',
    message="this number must contain 8 digits"
)

def validate_birth(v):
    if v >= timezone.localdate:
        raise ValidationError("date de naissance   n'est aps valide")
class Patient(User):
    national_id=models.CharField(max_length=8 ,unique=True ,validators=[NumberValidator])
    phone =models.CharField(max_length=8)
    birth_date=models.DateField(validators=[validate_birth])
    created_at =models.DateTimeField(auto_now=True)
    update_at=models.DateTimeField(auto_now=True)
    
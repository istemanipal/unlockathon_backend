from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=12)
    registration_number=models.CharField(max_length=9,unique=True)
    points=models.IntegerField(default=0)
    current_question=models.IntegerField(default=1)
    skips=models.IntegerField(default=3,validators=[MinValueValidator(0),MaxValueValidator(3)])

    def __str__(self):
        return self.username
    
    



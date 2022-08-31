from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Movie(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    year = models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(int(timezone.now().strftime('%Y')))])
    actor = models.ManyToManyField(to='Actor')
    
    def __str__(self):
        return self.title

class Actor(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    age = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(100)])
    
    def __str__(self):
        return self.name
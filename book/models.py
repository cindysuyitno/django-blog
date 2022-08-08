from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField(default=None)
    city = models.CharField(max_length=150)
    telephone = models.BigIntegerField(blank=True,null=True,default='-')
    email = models.EmailField(blank=True,null=True)

    def age(self):
        if self.birthday==None:
            return None
        else:
            return int(timezone.now().strftime('%Y')) - int(self.birthday.strftime('%Y'))

    author = models.OneToOneField(to='Author', on_delete=models.CASCADE)

class Publisher(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    year = models.IntegerField(validators=[MinValueValidator(1000),MaxValueValidator(int(timezone.now().strftime('%Y')))])

    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)
    author = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title
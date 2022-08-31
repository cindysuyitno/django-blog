from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    blog = models.ForeignKey(blank=True, null=True, to='Blog', related_name='posts', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    is_active = models.BooleanField(default=False)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    pos = models.ManyToManyField(to='Post', related_name='authors')

class Category(models.Model):
    title = models.CharField(max_length=100)
    post = models.ManyToManyField(to="Post", related_name='cat')



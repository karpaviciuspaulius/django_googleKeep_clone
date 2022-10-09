from django.db import models
from users.models import User
from django.urls import reverse

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('notes-home')
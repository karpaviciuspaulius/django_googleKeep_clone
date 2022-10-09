from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from groups.models import Group


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='note_pics', default='default.jpeg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Group)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk':self.pk})

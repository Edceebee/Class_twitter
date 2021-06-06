from django.db import models
from django.urls import reverse


class TwitterPost(models.Model):
    name = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_new', args=[str(self.id)])



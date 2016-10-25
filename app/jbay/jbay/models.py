from django.db import models
from django.utils import timezone

class shoes(models.Model):
    shoe = models.TextField()
    brand = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.shoe

class users(models.Model):
    name = models.TextField()
    address = models.TextField()
    cart = models.TextField()
    password = models.TextField(default="")
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

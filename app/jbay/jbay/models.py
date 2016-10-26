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
    name = models.CharField(max_length=30)
    password = models.TextField(default="")
    address = models.TextField()
    cart = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Authenticator(models.Model):
    authenticator = models.CharField(max_length=100, primary_key=True, default="")
    user_id = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.authenticator

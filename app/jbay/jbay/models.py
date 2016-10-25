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

class Authenticator(models.Model):
    auto_id = models.AutoField(primary_key=True, default="1")
    user_id = models.CharField(max_length=30)
    authenticator_val = models.TextField()
    # authenticator = models.TextField(primary_key=True)
    date_created = models.DateTimeField()
    # user = models.OneToOneField(users)

    def __str__(self):
        return self.authenticator

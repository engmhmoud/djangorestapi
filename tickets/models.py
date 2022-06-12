from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from django.conf import settings


class Movie(models.Model):
    hal = models.CharField(max_length=10)
    movie = models.CharField(max_length=10)
    date = models.DateField(auto_now=False, auto_now_add=False)


class Guest(models.Model):

    name = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)


class Reservation(models.Model):

    guest = models.ForeignKey(Guest, related_name="Reservation", on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="Reservation", on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def tocken_create(sender, instance, created, **kwargs):

    if created:
        Token.objects.create(user=instance)

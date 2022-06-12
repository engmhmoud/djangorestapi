from django.db import models


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

from rest_framework import serializers

from tickets.models import Movie, Guest, Reservation


class MovieSerializer(serializers.ModelSerializer):
    # hal = serializers.CharField()
    # movie = serializers.CharField( )
    # date = serializers.DateField( )
    class Meta:
        model = Movie
        fields = "__all__"


class GuestSerializer(serializers.ModelSerializer):

    # name = serializers.CharField()
    # mobile = serializers.CharField()

    class Meta:
        model = Guest

        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):

    # guest = serializers.ForeignKey(Guest, related_name="Reservation_guest", on_delete=models.CASCADE)
    # movie = serializers.ForeignKey(Movie, related_name="Reservation_Movie", on_delete=models.CASCADE)
    class Meta:
        model = Reservation
        fields = ["pk", "Reservation", "name", "movie"]

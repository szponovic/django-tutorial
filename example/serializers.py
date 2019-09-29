from rest_framework import serializers
from example.models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializing alle the Genres
    """

    class Meta:
        model = Genre
        fields = ('id', 'name', )


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializing all the movies
    """

    #genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ("id", "name", "year", "relased", "genre", "about", 'viewed', 'is_deleted')


class MovieMiniSerializer(serializers.ModelSerializer):
    """
    Serializing all the movies
    """

    class Meta:
        model = Movie
        fields = ("id", "name", 'is_deleted')
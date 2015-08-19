from rest_framework import serializers
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    "Make owner read only"
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'owner')

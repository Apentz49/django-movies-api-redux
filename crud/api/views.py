from django.contrib.auth.models import User
from rest_framework import generics, permissions
from movie.models import Movie
from movie.serializers import MovieSerializer
from api.permissions import IsOwnerOrSuperReadOnly


class ListCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrSuperReadOnly)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)

class DetailAndUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrSuperReadOnly)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
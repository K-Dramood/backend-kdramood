from rest_framework import generics, permissions
from .models import Drama, Review
from .serializers import DramaSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly
import random


class DramaList(generics.ListCreateAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DramaMood(generics.ListCreateAPIView):
    queryset = Drama.objects.filter(mood)
    serializer_class = DramaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     mood=self.request.mood
    #     return Drama.objects.filter(mood=mood)

    def get_random():
        return Drama.objects.order_by("?").first()


class DramaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drama.objects.all()
    serializer_class = DramaSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
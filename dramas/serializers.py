from rest_framework import serializers
from .models import Drama, Review

class DramaSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        read_only=True, many=True, view_name='review_detail')

    drama_url = serializers.ModelSerializer.serializer_url_field(
        view_name='drama_detail')
    
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Drama
        fields = ('id', 'title', 'mood', 'genre', 'synopsis', 'reviews', 'drama_url', 'user', 'photo')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    drama = serializers.HyperlinkedRelatedField(
        read_only=True, view_name='drama_detail')

    drama_id = serializers.PrimaryKeyRelatedField(
        source='drama', queryset=Drama.objects.all())

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ('id', 'user', 'posted', 'body', 'drama_id', 'owner', 'mood')
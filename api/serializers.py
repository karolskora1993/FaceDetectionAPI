from rest_framework import serializers
from .models import Face


class FaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Face
        fields = ('id', 'image', 'date_created')
        read_only_fields = ('id', 'date_created')

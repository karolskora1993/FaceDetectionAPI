from rest_framework import serializers
from .models import Face

class FaceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('image', 'date_created')
        read_only_fields = ('date_created')
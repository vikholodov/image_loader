from rest_framework import serializers

from core.models import Image


class ImageSerializer(serializers.ModelSerializer):
    width = serializers.ReadOnlyField()
    height = serializers.ReadOnlyField()
    size = serializers.ReadOnlyField()
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = '__all__'
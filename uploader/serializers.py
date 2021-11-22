from rest_framework import serializers
from .models import Image

def size_validator(value):
    if value.size > 1024*200:
        raise serializers.ValidationError('error')
    
class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(validators=[size_validator])
    class Meta:
        model = Image
        fields = '__all__'
        
        
        
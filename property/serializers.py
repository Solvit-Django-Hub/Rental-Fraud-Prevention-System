from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['landlord_id', 'address', 'description', 'listing_price']
        read_only_fields = ['property_id']
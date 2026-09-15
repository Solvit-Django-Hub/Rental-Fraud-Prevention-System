from rest_framework import serializers
from .models import Landlord

class LandlordSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Landlord
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        read_only_fields = ['landlord_id', 'is_verified', 'verification_date']
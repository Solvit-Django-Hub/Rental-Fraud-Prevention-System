from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['landlord_id', 'tier', 'start_date', 'end_date','price']
        read_only = ['subscription_id', 'is_active']
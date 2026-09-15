from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['property_id', 'tenant_id', 'overall_rating','responsiveness_rating','property_accuracy_rating', 'comment']
        read_only = ['review_id', 'created_at']
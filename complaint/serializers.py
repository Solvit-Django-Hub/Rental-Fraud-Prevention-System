from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['lease_id', 'complaint_type', 'status']
        read_only= ['complaint_id', 'created_at', 'resolved_at']
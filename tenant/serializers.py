from rest_framework import serializers
from .models import Tenant

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        read_only_fields = ['tenant_id']
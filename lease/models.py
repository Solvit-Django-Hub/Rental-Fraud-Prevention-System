from django.db import models
from tenant.models import Tenant
from property.models import Property

class Lease(models.Model):
    PENDING = 'Pending Signature'
    SIGNED = 'Signed / Future'
    ACTIVE = 'Active / Current'
    DELINQUENT = 'Past Due'
    NOTICE = 'Notice Given'
    EXPIRED = 'Expired'
    TERMINATED = 'Terminated'
    Status_posted=[
        (PENDING, 'Pending Signature'),
        (SIGNED, 'Signed / Future'),
        (ACTIVE, 'Active / Current'),
        (DELINQUENT, 'Past Due'),
        (NOTICE, 'Notice Given'),
        (EXPIRED, 'Expired'),
        (TERMINATED, 'Terminated'),
    ]
        
    lease_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    property_id= models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant_id= models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    deposit_amount= models.DecimalField(max_digits=10, decimal_places=2)
    status= models.CharField(max_length=30, choices=Status_posted)
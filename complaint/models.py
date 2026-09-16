from django.db import models
import uuid
from lease.models import Lease

class Complaint(models.Model):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    RESOLVED = 'Resolved'
    REJECTED = 'Rejected'

    Status_choices = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (RESOLVED, 'Resolved'),
        (REJECTED, 'Rejected'),
    ]
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Complaint ID")
    lease_id = models.ForeignKey(Lease, on_delete=models.CASCADE)
    complain_type = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=Status_choices, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
# Create your models here.

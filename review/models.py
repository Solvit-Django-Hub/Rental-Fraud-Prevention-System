from django.db import models
import uuid
from lease.models import Lease

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Review ID")
    lease_id = models.ForeignKey(Lease, on_delete=models.CASCADE)
    deposit_returned = models.BooleanField()
    property_accuracy_rating= models.IntegerField()
    responsiveness_rating = models.IntegerField()
    overall_rating = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 



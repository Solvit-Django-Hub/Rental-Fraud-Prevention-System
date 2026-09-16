from django.db import models
from landlord.models import Landlord

class Subscription(models.Model):
    subscription_id = models.BigAutoField(auto_created=True,primary_key=True, unique=True, serialize=False, verbose_name='ID')
    landlord_id = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    tier = models.CharField(max_length=30)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    price = models.FloatField()
    

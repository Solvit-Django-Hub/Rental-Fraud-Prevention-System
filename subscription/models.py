from django.db import models

class Subscription(models.Model):
    subscription_id = models.BigAutoField(auto_created=True, unique=True, serialize=False, verbose_name='ID')
    landlord_id = models.ForeignKey('landlord_id.Landlord', on_delete=models.CASCADE)
    tier = models.CharField(max_length=30)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    price = models.FloatField()
    

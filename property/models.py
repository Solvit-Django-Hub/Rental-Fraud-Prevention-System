from django.db import models

class Property(models.Model):
    property_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    landlord_id = models.ForeignKey('Landlord', on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    description = models.TextField()
    listing_price = models.FloatField()

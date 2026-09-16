from django.db import models

class Tenant(models.Model):
    tenant_id = models.BigAutoField(auto_created=True,primary_key=True, unique=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    
    
    
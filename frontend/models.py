from django.db import models

# Create your models here.



class B_users(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    Btc_address = models.CharField(max_length=38, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    public_key = models.CharField(max_length=500, blank=True, null=True)
    private_key = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f'self.fullName'



class Admin_address(models.Model):
    address = models.CharField(max_length=400)

    def __str__(self):
        return str(self.address)
from django.db import models

# Create your models here.



class B_users(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=38)
    phone_number = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'self.fullName'

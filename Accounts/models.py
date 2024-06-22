from django.db import models
# from django.contrib.auth import User
from django.contrib.auth.models import User




# Create your models here.

class DepositModels(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='account')
    deposit = models.DecimalField(default=0,decimal_places=2,max_digits=12)

    def __str__(self) -> str:
        return self.user.first_name


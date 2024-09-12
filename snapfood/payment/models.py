from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date



class Copun(models.Model):
    code = models.CharField(max_length=15 , unique=True)
    percent = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    expire_date = models.DateField()
    user = models.ManyToManyField(User)
    
    @property
    def activation_status(self):
        return date.today() <= self.expire_date
    
    def __str__(self) -> str:
        return self.code

class Factor(models.Model):
    date = models.DateField()
    order_id = models.IntegerField(unique=True)
    status = models.BooleanField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True , null=True)
    copun = models.ForeignKey(Copun , on_delete= models.CASCADE , null=True , blank=True)
    user = models.ForeignKey(User , on_delete= models.PROTECT)

    
    

class Transaction(models.Model):
    dargah = models.CharField(max_length=20)
    trans_id = models.CharField(max_length=10 ,null=True , blank=True)
    factor = models.ForeignKey(Factor ,on_delete=models.PROTECT , related_name= "factor").
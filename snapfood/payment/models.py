from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    pass
class Usr(models.Model):
    email = models.EmailField(default=None)

    def __str__(self) -> str:
        return self.email

class Copun(models.Model):
    code = models.CharField(max_length=15)
    percent = models.IntegerField()
    expire_date = models.DateField()
    user = models.ManyToManyField(User)
    
    
class Factor(models.Model):
    date = models.DateField()
    # order = models.ForeignKey(Order ,on_delete=models.PROTECT)
    order_id = models.IntegerField()
    status = models.BooleanField()
    price = models.FloatField()
    copun = models.ForeignKey(Copun , on_delete= models.CASCADE )
    user = models.ForeignKey(User , on_delete= models.PROTECT)



    def __str__(self) -> str:  #-------------baraye inke moghe didan esmesh biyad
        return self.code
    

class Transaction(models.Model):
    dargah = models.CharField(max_length=20)
    trans_id = models.CharField(max_length=10)
    copun = models.ForeignKey(Copun , on_delete=models.CASCADE , related_name="copun")
    factor = models.ForeignKey(Factor ,on_delete=models.PROTECT , related_name= "factor")
    user = models.ForeignKey(User , on_delete=models.PROTECT)
from django.db import models


class date(models.Model):
    date=models.DateField('date')

    def __str__(self):
        return  str(self.date)
    


class vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)  
    v_vegetable_name = models.CharField(max_length=20)
    v_price = models.IntegerField()
    v_quantity = models.IntegerField()
    v_total = models.IntegerField()
    payment_status = models.CharField(max_length=10, default="Unpaid")  # New field

    def __str__(self):
        return f"{self.id} - {self.name}"

    

class mgt(models.Model):
    date=models.ForeignKey(date,blank=False,null=False,on_delete=models.CASCADE)
    vendor=models.ForeignKey(vendor,blank=False,null=False,on_delete=models.CASCADE)
    vehicle_number=models.CharField(max_length=10)
    vegetable_name=models.CharField(max_length=20)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total=models.IntegerField()
  
    def __str__(self):
        return  str(self.vegetable_name)





class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # In production, use Django's authentication system for security.

    def __str__(self):
        return self.username
    
from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Store securely in production

    def __str__(self):
        return self.username

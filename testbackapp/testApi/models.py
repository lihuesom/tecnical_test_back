from django.db import models
from django.contrib.auth.hashers import check_password as django_check_password

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    identification = models.IntegerField()
    password = models.CharField(max_length=100)
    created  = models.DateTimeField(auto_now_add=True)

    def check_password(self, password,hashed_password):
        return django_check_password(password, hashed_password)


class Offer(models.Model):
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    value = models.IntegerField()
    product_number = models.IntegerField()
    days_late = models.IntegerField()
    created  = models.DateTimeField(auto_now_add=True)


class Agreement(models.Model):
    offer_id = models.ForeignKey(Offer,on_delete=models.CASCADE)
    value = models.IntegerField()
    payment_date =  models.DateTimeField()
    state = models.BooleanField()
    created  = models.DateTimeField(auto_now_add=True)



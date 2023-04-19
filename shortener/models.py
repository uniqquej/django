import random
import string
from django.db import models
from django.contrib.auth.models import User as U
# Create your models here.
class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Organization(models.Model):
    class Industries(models.TextChoices):
        PERSONAL = 'personal'
        RETAIL = 'retail'
        MANUFACTURING = 'manufacturing'
        IT = 'it'
        OTHERS = 'others'
    name = models.CharField(max_length=50)
    indusrty = models.CharField(max_length=15, choices=Industries.choices, default=Industries.OTHERS)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Users(models.Model):
    user = models.OneToOneField(U, on_delete=models.CASCADE)
    payplan = models.OneToOneField(PayPlan, on_delete=models.DO_NOTHING, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
 
class EmailVerification(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, null=True)
    verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Categories(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ShortenedUrls(models.Model):
    class UrlCreatedVia(models.TextChoices):
        WEBSITE='web'
        TELEGRAM='telegram'

    def rand_string():
        str_pool = string.digits + string.ascii_letters
        return ("".join([random.choice(str_pool) for _ in range(6)])).lower()
        
    nick_name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, null=True)
    prefix = models.CharField(max_length=50)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)
    target_url = models.CharField(max_length=2000)
    shortened_url = models.CharField(max_length=6, default=rand_string)
    created_via = models.CharField(max_length=8, choices=UrlCreatedVia.choices, default=UrlCreatedVia.WEBSITE)
    expired_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
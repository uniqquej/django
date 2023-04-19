from django.contrib import admin
from shortener.models import Users, PayPlan
# Register your models here.
admin.site.register(Users)
admin.site.register(PayPlan)
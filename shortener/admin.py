from django.contrib import admin
from shortener.models import Users, PayPlan, Statistic, TrackingParams
# Register your models here.
admin.site.register(Users)
admin.site.register(PayPlan)
admin.site.register(Statistic)
admin.site.register(TrackingParams)
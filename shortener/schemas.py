from rest_framework.permissions import OR
from shortener.models import Organization, PayPlan
from ninja import Schema
from django.contrib.auth.models import User as U
from ninja.orm import create_schema

OrganizationSchema = create_schema(Organization) #organization 모델을 그대로 가져옴
# OrganizationSchema = create_schema(Organization, exclude=['password',])

class User(Schema):
    id : int
    full_name : str = None
    organization: OrganizationSchema = None

class TelegramUpdateSchema(Schema):
    username: str
    
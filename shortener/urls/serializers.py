from django.contrib.auth.models import User
from shortener.models import Users, ShortenedUrls
from shortener.utils import url_count_changer
from rest_framework import serializers

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
        
class UserSerializer(serializers.ModelSerializer):
    user = UserBaseSerializer(read_only=True)
    
    class Meta:
        model = Users
        fields = ['id','url_count','organization','user']

class UrlListSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    
    class Meta:
        model = ShortenedUrls
        fields = ['id','nick_name','prefix','shortened_url','creator','click','create_via','expired_at']

class UrlCreateSerializer(serializers.Serializer):
    nick_name = serializers.CharField(max_length=50)
    target_url = serializers.CharField(max_length=100)
    category = serializers.IntegerField(required=False)
    
    def create(self, request, data, commit=True):
        instance = ShortenedUrls()
        instance.creator_id = request.user.id
        instance.category = data.get('category',None)
        instance.target_url = data.get('target_url').strip()
        
        if commit:
            try:
                instance.save()
            except Exception as e:
                print(e)
            else:
                url_count_changer(request, True)
        return instance
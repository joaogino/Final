from rest_framework import serializers
from .models import *

class commentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'

class todosSerializer(serializers.ModelSerializer):
    class Meta:
        model = todos
        fields = '__all__'

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class postsSerializer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'
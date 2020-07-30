from .models import myBaseUser
from  rest_framework import serializers


class myBaseUserSerializer(serializers.ModelSerializer):
    model = myBaseUser
    fields = "__all__"

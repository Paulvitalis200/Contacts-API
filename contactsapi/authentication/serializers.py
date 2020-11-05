from rest_framework import seriailizers
from django.contrib.auth.models import User

class UserSerializer(seriailizers.ModelSerializer):
    password = seriailizers.CharField(
        max_length=65,min_length=6,write_only=True)
    email = seriailizers.EmailField(max_length=255,min_length=4)
    first_name = seriailizers.CharField(max_length=255,min_length=2)
    last_name = seriailizers.CharField(max_length=255,min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise seriailizers.ValidationError(
            {'email', ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(validated_data)
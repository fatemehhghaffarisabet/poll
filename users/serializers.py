from rest_framework import serializers

from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        

    def validate(self, data):
        confirm_password = data.pop("confirm_password")
        if data['password'] != confirm_password:
            raise serializers.ValidationError("Passwords must match.")

        return data
    
    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.set_password(self.validated_data.get("password"))
        user.save()
        return user
    
class UserLogInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
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
    
class EditProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_old_password(self, data):
        user = self.context['request'].user
        if not user.check_password(data):
            raise serializers.ValidationError("Old password is not correct")
        return data

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New password and confirm password do not match")
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data.get("new_password"))
        user.save()
        return user
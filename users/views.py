from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSignUpSerializer

class UserSignupView(generics.GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
        
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
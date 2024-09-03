from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignUpSerializer, UserLogInSerializer, EditProfileSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class UserSignupView(generics.GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
        
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
class UserLogInView(generics.GenericAPIView):
    serializer_class = UserLogInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
                
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({'error': 'invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access),
        }, status=status.HTTP_200_OK)
    
class UserLogOutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class RefreshTokenView(generics.GenericAPIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            access = token.access_token

            return Response({
                'access': str(access),
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EditProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = EditProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, is_partial=False):
        serializer = self.serializer_class(request.user, request.data, partial=is_partial)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
        
        serializer.save()
        return Response({"data": request.data}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        return self.update(request, is_partial=True)
        
    def put(self, request, *args, **kwargs):
        return self.update(request)
    
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"data": request.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

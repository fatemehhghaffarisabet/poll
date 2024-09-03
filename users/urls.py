from .views import UserSignupView, UserLogInView, UserLogOutView, RefreshTokenView, EditProfileView, ChangePasswordView
from django.urls import path, include

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLogInView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh'),
    path('profile/', EditProfileView.as_view(), name='edit-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]

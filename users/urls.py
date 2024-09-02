from .views import UserSignupView, UserLogInView
from django.urls import path, include

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLogInView.as_view(), name='login'),
]
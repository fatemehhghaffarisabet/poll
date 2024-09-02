from .views import UserSignupView
from django.urls import path, include

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='signup'),
]
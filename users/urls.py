from django.urls import path
from users.views import Signup, Login, Logout, Change_password

app_name = 'users'

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('change_password/', Change_password.as_view(), name='change_password')
]
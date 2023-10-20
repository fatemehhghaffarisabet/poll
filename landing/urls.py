from django.urls import path

from landing.views import Home


app_name = 'landing'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
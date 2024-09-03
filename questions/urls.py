from .views import QuestionView
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', QuestionView.as_view(), name='update-detail-delete-question'),
    path('', QuestionView.as_view(), name='list-post-question'),
]

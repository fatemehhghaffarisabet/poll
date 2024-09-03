from .views import QuestionView, ChoiceView
from django.urls import path, include

urlpatterns = [
    path('<int:pk>/', QuestionView.as_view(), name='update-detail-delete-question'),
    path('', QuestionView.as_view(), name='list-post-question'),
    path('<int:question_id>/choices/', ChoiceView.as_view(), name='list-post-choice'),
    path('<int:question_id>/choices/<int:pk>/', ChoiceView.as_view(), name='update-choice'),
    path('choices/<int:pk>/', ChoiceView.as_view(), name='delete-choice'),
]

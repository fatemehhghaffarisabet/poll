from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.QuestionView.as_view(), name='update-detail-delete-question'),
    path('', views.QuestionView.as_view(), name='list-post-question'),
    path('<int:question_id>/choices/', views.ChoiceView.as_view(), name='list-post-choice'),
    path('<int:question_id>/choices/<int:pk>/', views.ChoiceView.as_view(), name='update-choice'),
    path('choices/<int:pk>/', views.ChoiceView.as_view(), name='delete-choice'),
    path('<int:question_id>/vote/<int:choice_id>/', views.vote, name='vote'),
    path('<int:question_id>/unvote/<int:choice_id>/', views.unvote, name='unvote'),
    path('<int:question_id>/detail/', views.vote_detail, name='vote-detail'),
    path('<int:question_id>/change-status/', views.change_status, name='change-status'),
    path('<int:question_id>/result/', views.see_result, name='see-result'),
]

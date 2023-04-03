from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('questions/', views.questions_list, name='questions_list'),
    path('questions/<int:pk>/', views.question_detail, name = 'questions_detail')
]

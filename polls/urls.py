from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('questions/', views.questions_list),
    path('questions/<int:pk>/', views.question_detail, name = 'questions_detail')
]

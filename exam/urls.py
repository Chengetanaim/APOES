from django.urls import path, include
from . import views

app_name = 'exam'

urlpatterns = [
    path('', views.index, name='index'),
    path('multiple_choice/<int:exam_id>/', views.multiple_choice, name='multiple_choice'),
    path('structured/<int:exam_id>/', views.structured, name='structured'),
    path('proctor/', views.proctor, name='proctor'),
    path('alert/', views.alert, name='alert'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('students/', views.all_students, name='all_students'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
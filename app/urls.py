from django.urls import re_path,path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('info/<str:key>/', views.home, name='home'),
    path('createRoom/', views.createRoom, name='createRoom'),
    path('joinRoom/', views.joinRoom, name='joinRoom'),
]
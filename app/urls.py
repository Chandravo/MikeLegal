from django.urls import re_path,path
from . import views
urlpatterns = [
    path('info/<str:key>/', views.home, name='home'),
]
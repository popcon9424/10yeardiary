from django.urls import path
from . import views


app_name = 'uesrs'


urlpatterns = [
    path('register/', views.register, name='register'),
]

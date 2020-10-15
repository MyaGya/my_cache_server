from django.urls import path
from . import views

app_name = 'cache_video'
urlpatterns = [
    path('', views.main, name='main')
]
from django.urls import path, include
from . import views

app_name = 'news_api'

urlpatterns = [
	path('api/', views.api, name="api"),
	path('news/', views.news, name="news"),
]
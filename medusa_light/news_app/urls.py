from django.urls import path
from news_app import views 

app_name = "news_app"

urlpatterns = [
    path('', views.home, name='homeviews'),
    path('add_news/', views.add_news, name='addnews'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('all-tweets', views.AllTweets.as_view(), name='all-tweets'),
]

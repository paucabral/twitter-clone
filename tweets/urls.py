from django.urls import path
from . import views

urlpatterns = [
    path('all-tweets', views.AllTweets.as_view(), name='all-tweets'),
    path('delete-tweet/<id>', views.deleteTweet, name='delete-tweet'),
    path('edit-tweet/<id>', views.EditTweet.as_view(), name='edit-tweet'),
]

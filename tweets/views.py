from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *

# Create your views here.


class AllTweets(View):
    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.all().order_by('-date_created')
        return render(request, template_name='tweets/all-tweets.html', context={'tweets': tweets})

    def post(self, request, *args, **kwargs):
        pass

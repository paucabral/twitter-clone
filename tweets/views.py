from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class AllTweets(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.all().order_by('-date_created')
        return render(request, template_name='tweets/all-tweets.html', context={'tweets': tweets})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        pass

from django.shortcuts import render, redirect
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
        user = request.user.profile
        msg = request.POST.get('tweet')
        tweet = Tweet(user=user, msg=msg)
        tweet.save()
        return redirect('/tweets/all-tweets')


@login_required(login_url='/')
def deleteTweet(request, id):
    if request.method == "POST":
        tweet = id
        tweet_instance = Tweet.objects.filter(id=tweet)
        tweet_instance.delete()
    return redirect('/tweets/all-tweets')


class EditTweet(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        tweet_id = self.kwargs['id']
        tweet = Tweet.objects.get(id=tweet_id)
        tweet_id = tweet.user.id
        tweet_msg = tweet.msg
        return render(request, template_name='tweets/update-tweet.html', context={'tweet_id': tweet_id, 'tweet_msg': tweet_msg})

    @method_decorator(login_required(login_url='/'))
    def post(self, request, *args, **kwargs):
        tweet_id = self.kwargs['id']
        tweet = Tweet.objects.get(id=tweet_id)
        user = request.user.profile
        tweet_user = tweet.user.id
        msg = request.POST.get('tweet_msg')

        if user.id == tweet_user:
            tweet.msg = msg
            tweet.save()
            return redirect('/tweets/all-tweets')


class UserTimeline(View):
    @method_decorator(login_required(login_url='/'))
    def get(self, request, *args, **kwargs):
        profile_id = self.kwargs['id']
        profile = Profile.objects.get(id=profile_id)
        tweets = Tweet.objects.filter(
            user=profile_id).order_by('-date_created')
        return render(request, template_name='tweets/user-timeline.html', context={'profile': profile, 'tweets': tweets})

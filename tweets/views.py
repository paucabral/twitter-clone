from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class AllTweets(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='tweets/all-tweets.html', context={})

    def post(self, request, *args, **kwargs):
        pass

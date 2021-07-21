from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class Login(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('login')

    def post(self, request, *args, **kwargs):
        pass

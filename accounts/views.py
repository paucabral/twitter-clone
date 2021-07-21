from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/login.html', context={})

    def post(self, request, *args, **kwargs):
        pass

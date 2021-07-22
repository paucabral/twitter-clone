from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import CreateUserForm
from .models import *
from django.contrib import messages

# Create your views here.


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/login.html', context={})

    def post(self, request, *args, **kwargs):
        pass


class Register(View):
    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(request, template_name='accounts/register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            profile = Profile(user=user, first_name=first_name,
                              last_name=last_name, email=email, username=username)
            profile.save()
            return redirect('/registration-success/')
        else:
            messages.error(request, 'There was an error.')
        return render(request, template_name='accounts/register.html', context={'form': form})


class RegistrationSuccess(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='accounts/registration-success.html', context={})

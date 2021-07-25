from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('registration-success/', views.RegistrationSuccess.as_view(),
         name='registration-success'),
    path('logout/', views.logoutUser, name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset-password.html"),
         name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset-password-sent.html"),
         name="password_reset_done"),
    path('reset-password-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset-password-confirm.html"), name="password_reset_confirm"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset-password-complete.html"),
         name="password_reset_complete"),
    path('profile/', views.Profile.as_view(), name='profile'),
]

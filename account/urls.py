from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views
from .forms import (PwdResetConfirmForm, PwdResetForm, UserLoginForm)

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html',
                                                form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/', AccountRegister.as_view(), name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', AccountActivate.as_view(), name='activate'),
    # Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html",
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='account/user/password_reset_email.html',
                                                                 form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                                                                success_url='/account/password_reset_complete/',
                                                                                                form_class=PwdResetConfirmForm),
         name="password_reset_confirm"),
    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="reset_status.html"), name='password_reset_done'),
    path('password_reset_complete/',
         TemplateView.as_view(template_name="reset_status.html"), name='password_reset_complete'),
    # User dashboard
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('profile/edit/', EditDetails.as_view(), name='edit_details'),
    path('profile/delete_user/', DeleteUser.as_view(), name='delete_user'),
    path('profile/delete_confirm/', TemplateView.as_view(template_name="delete_confirm.html"), name='delete_confirmation'),
]
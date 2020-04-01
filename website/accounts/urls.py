from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='accounts-login'),

    path('register/', views.register_view, name='accounts-register'),
    path('forgot/', views.forgot_view, name='accounts-forgot'),
    path('reset/', views.reset_view, name='accounts-reset'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html'
         ),
         name='password_reset'),


    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-change/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/password_change.html'),
         name='password_change'),

    path('password-change/done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/password_change_done.html'),
         name='password_change_done'),



    path('profile/', views.profile_view, name='accounts-profile'),
    path('logout/', views.logout_view, name='accounts-logout'),
]

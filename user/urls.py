from django.urls import path
from . import views

from .views import (login_view, signup_view, verify_email,
                    verification_alert, verification_resend, logout_view, welcome_view, group_page as groups_view,
                    ResetPasswordView
                    )
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('email/verify/', verify_email, name='verify-email'),

    path('email/verification/resend/', verification_resend, name='resend-verification'),
    path('email/verification-alert/', verification_alert, name='verification-alert'),

    path('password/reset/', ResetPasswordView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='html/authentication/password-reset-confirm.html'),
            name='password_reset_confirm'),
     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='html/authentication/password-reset-complete.html'),
         name='password_reset_complete'),

    path('welcome/', welcome_view, name='welcome'),
    path('groups/', groups_view, name='groups'),
    path('create-group/', views.create_group, name='create_group'),
    path('join-group/<int:group_id>/', views.join_group, name='join_group'),
    path('leave-group/<int:group_id>/', views.leave_group, name='leave_group')
]

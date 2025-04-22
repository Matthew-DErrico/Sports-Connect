import jwt
import json

from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.utils.encoding import force_str
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .models import User
from .models import Group
from .forms import CustomUserCreationForm
from .forms import GroupForm
from .forms import Group
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from utils.token_generator import send_token


def login_view(request):
    next_url = request.GET.get('next', '')

    if request.user.is_authenticated:
        #if next_url and next_url != request.path:
            #return redirect(next_url)
        
        #return redirect('home')
        return redirect('welcome')

    if request.method == "GET":
        return render(request, 'html/authentication/login.html', {
            'next': next_url
        })

    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    
    #if User.objects.filter(email=email, is_active=False).exists():
        #url = reverse('verification-alert') + f'?email={email}'
        
        #return redirect(url)
        # is_active=False deals with user verification.

    if user is not None:
        login(request, user)
                
        #if next_url and next_url != request.path:
            #return redirect(next_url)
        
        #return redirect('home')
        return redirect('welcome')

    return render(request, 'html/authentication/login.html', {'error': f'Invalid email or password'})


def logout_view(request):
    logout(request)

    return redirect('home')


@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.method == "GET":
        return render(request, 'html/authentication/signup.html')
    
    else:   
        form = CustomUserCreationForm(request.POST)
       
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                login(request, user) # login user after signup
                return redirect('welcome')
            
            # login(request, user) # don't login user unless the user has verified their email
            #send_token(username)

            #url = reverse('verification-alert') + f'?email={username}'
            #return redirect(url)

        return render(request, 'html/authentication/signup.html', context={'errors': form.errors})


def verification_alert(request):
    """
        alert that the user has to verify their email
    """
    email = request.GET.get('email') or ''
    return render(request, 'html/authentication/verification-alert.html', context={'from_email': settings.EMAIL_HOST,
                                                                'to_email': email   
                                                            })


@require_http_methods(["GET", "POST"])
def verification_resend(request):
    """
        resend the confirmation email
    """

    if request.method == "POST":

        email = request.POST.get('email')

        user = User.objects.filter(email=email)

        if not user.exists():

            return render(request, 'html/authentication/resend-confirmation.html', {'error': f'The email {email} is not registered'})

        if user.filter(is_active=True):
            return render(request, 'html/authentication/resend-confirmation.html', {'error': f'The email {email} is already active'})

        send_token(email)
        url = reverse('verification-alert') + f'?email={email}'
        return redirect(url)

    return render(request, 'html/authentication/resend-confirmation.html')


def verify_email(request):
    token = request.GET.get('token')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        email = payload['email']

        user = get_user_model().objects.get(email=email)
        user.is_active = True
        user.save()

        send_token(email)

        return redirect('login')  # Redirect to a success page

    except jwt.ExpiredSignatureError:
        return render(request, 'html/authentication/email-verification.html', context={'error': 'Token expired, request another'})

    except (jwt.DecodeError, Exception):
        return render(request, 'html/authentication/email-verification.html', context={'error': 'Unknown error occurred, request a new token'})
    

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user  # Set current user as owner
            group.save()
            return redirect('groups')
    else:
        form = GroupForm()

    return render(request, 'create_group.html', {'form': form})


@login_required
def group_page(request):
    owned_groups = Group.objects.filter(owner=request.user)
    joined_groups = Group.objects.filter(members=request.user).exclude(owner=request.user)
    all_groups = Group.objects.exclude(owner=request.user).exclude(members=request.user)

    """for g in all_groups:
        print(f"Group: {g.name}, Owner: {g.owner} (ID: {g.owner.id})")

    owned_groups = Group.objects.filter(owner=request.user)
    print(f"Owned Groups: {owned_groups}")"""

    return render(request, 'groups.html', {
        'owned_groups': owned_groups,
        'joined_groups': joined_groups,
        'all_groups': all_groups
    })


@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.add(request.user)
    return redirect('groups')


@login_required
def leave_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.remove(request.user)
    return redirect('groups')


@login_required
@require_POST
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id, owner=request.user)
    group.delete()
    return redirect('groups')


def welcome_view(request):
    email = request.user.email
    username = email.split('@')[0] if '@' in email else email
    return render(request, 'html/welcome.html', {'username': username})


def groups_view(request):
    username = request.user.email.split('@')[0] if request.user.is_authenticated else "User"
    return render(request, 'html/groups.html', {'username': username})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'html/authentication/password-reset-request.html'
    email_template_name = 'html/authentication/password-reset-email.html'
    # subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password-reset')
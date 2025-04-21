from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from .models import Group


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)

        from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'sport', 'competition_level', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
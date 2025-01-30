# filepath: /home/rsiurek/szu/accounts/forms.py
from django import forms
from django.core.validators import RegexValidator
from .models import Collaborator

class CollaboratorForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    nip = forms.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid NIP (10 digits).')]
    )
    name = forms.CharField(
        max_length=255,
        validators=[RegexValidator(r'^[a-zA-Z\s]+$', 'Enter a valid name (letters and spaces only).')]
    )
    contact = forms.CharField(
        max_length=255,
        validators=[RegexValidator(r'^[a-zA-Z0-9\s@.-]+$', 'Enter a valid contact (letters, numbers, spaces, @, ., and - only).')]
    )

    class Meta:
        model = Collaborator
        fields = ['username', 'password', 'nip', 'name', 'contact']
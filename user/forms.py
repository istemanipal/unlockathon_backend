from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class CustomUserCreationForm(UserCreationForm):

    username=forms.CharField(
        widget=forms.TextInput(attrs={'class':'input100','placeholder':'UserName','autofocus':''}),
        help_text="<i class='fa fa-user' aria-hidden='true'></i>",
    )
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'input100','placeholder':'Email'}),
        help_text="<i class='fa fa-envelope' aria-hidden='true'></i>"
    )
    first_name=forms.CharField(
        widget=forms.TextInput(attrs={'class':'input100','placeholder':'First Name'}),
        help_text="<i class='fa fa-user' aria-hidden='true'></i>"
    )
    last_name=forms.CharField(
        widget=forms.TextInput(attrs={'class':'input100','placeholder':'Last Name'}),
        help_text="<i class='fa fa-user' aria-hidden='true'></i>"
    )
    registration_number=forms.CharField(
        widget=forms.TextInput(attrs={'class':'input100','placeholder':'Registration Number'}),
        help_text="<i class='fa fa-user-circle' aria-hidden='true'></i>"
    )
    phone=forms.CharField(
        widget=forms.TextInput(attrs={'class':'input100','placeholder':'Phone Number Without +'}),
        help_text="<i class='fa fa-mobile-phone' aria-hidden='true'></i>"
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Enter Password'}),
        help_text="<i class='fa fa-lock' aria-hidden='true'></i>"
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Enter Password again'}),
        help_text="<i class='fa fa-lock' aria-hidden='true'></i>"
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus",None)
    class Meta:
        model=CustomUser
        fields=['email','username','first_name','last_name','registration_number','phone','password1']


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input100','placeholder':'Username/Registration Number'}),
        help_text="<i class='fa fa-user' aria-hidden='true'></i>",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'}),
        help_text="<i class='fa fa-lock' aria-hidden='true'></i>"
    )

    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s or Registration Number and Password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
    }
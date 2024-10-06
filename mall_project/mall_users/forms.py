from django import forms
from django.contrib.auth.hashers import make_password, check_password
from .models import MallUserClass



class UserRegisterForm(forms.Form):
    register_email = forms.EmailField(
        error_messages={
            'required': 'Please input email field'
        },
        widget=forms.EmailInput, label='Email'
    )

    register_pw = forms.CharField(
        error_messages={
            'required': 'Please input password'
        },
        widget=forms.PasswordInput, label='Password'
    )

    re_password = forms.CharField(
        error_messages={
            'required': 'Please confirm password'
        },
        widget=forms.PasswordInput, label='Confirm Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        cleaned_email = cleaned_data.get('register_email')
        cleaned_pw = cleaned_data.get('register_pw')
        cleaned_re_pw = cleaned_data.get('re_password')

        if cleaned_pw and cleaned_re_pw:
            if cleaned_pw != cleaned_re_pw:
                self.add_error('re_password', 'Password does not match')
            else:
                registering_user = MallUserClass(
                    user_email=cleaned_email,
                    user_pw=make_password(cleaned_pw)
                )
                registering_user.save()


class LoginForm(forms.Form):
    input_email = forms.EmailField(
        error_messages={
            'required': 'Please input email field'
        },
        widget=forms.EmailInput, label='Email'
    )

    input_pw = forms.CharField(
        error_messages={
            'required': 'Please input password'
        },
        widget=forms.PasswordInput, label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        cleaned_email = cleaned_data.get('input_email')
        cleaned_pw = cleaned_data.get('input_pw')

        if cleaned_email and cleaned_pw:
            try:
                login_user = MallUserClass.objects.get(user_email=cleaned_email)
            except:
                self.add_error('user_email', 'Cannot find email')
                return

            if not check_password(cleaned_pw, login_user.user_pw):
                self.add_error('user_pw', 'Password does not match')
            else:
                self.input_email = login_user.user_email
                login_user.save()
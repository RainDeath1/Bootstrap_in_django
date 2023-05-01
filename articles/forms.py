from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        help_text='Ваш пароль не должен быть слишком похож на другую личную информацию, быть длиной не менее 8 символов, не может быть общепринятым паролем и не может состоять только из цифр.'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        help_text='Введите тот же самый пароль для проверки.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
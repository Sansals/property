# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Подключаем модель User
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, ModelForm


# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Введите email',
                                                                           'id': 'user_email_inp'}))
    username = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control',
                                                                            'placeholder': 'Введите имя нового пользователя',
                                                                            'id': 'user_username_inp'}))
    password1 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                  'placeholder': 'Введите пароль',
                                                                                  'id': 'user_pass1_inp'}))
    password2 = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                 'placeholder': 'Подтвердите пароль',
                                                                                 'id': 'user_pass2_inp'}))


    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2')

class AuthenticationUser(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите логин',
                                                             'id': 'user_login_inp'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введите пароль',
                                                                 'id': 'user_password_inp'}))

class Authentication_code(forms.Form):
    auth_code = forms.CharField(label='Код подтверждения', widget=forms.TextInput(attrs={'class': 'form-input'}))

class AddEmailForm(forms.Form):
    email = forms.EmailField(label='Введите свой email', widget=forms.TextInput(attrs={'class': 'form-input'}))

class FormPasswordReset(forms.Form):
    email = forms.EmailField(label='Введите свой email', widget=forms.TextInput(attrs={'class': 'form-input'}))

class FormPasswordResetConfirm(forms.Form):
    password1= forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    code = forms.CharField(label='Введите код с почты', widget=forms.TextInput(attrs={'class': 'form-input'}))

class UsersData(forms.Form):
    first_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                         'id': "exampleInputEmail1",
                                                                                         'placeholder':'Введите имя'
                                                                                         }))
    last_name = forms.CharField(label='Фамилия пользователя', widget=forms.TextInput(attrs={'class':'form-control',
                                                                                            'id':'exampleInputPassword1',
                                                                                            'placeholder':'Введите фамилию'
                                                                                            }))
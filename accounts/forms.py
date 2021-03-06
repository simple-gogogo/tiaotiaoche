from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    """登录表单类"""

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})

    def clean(self):
        username = self.cleaned_data['username']
        if not get_user_model().objects.filter(username=username):
            raise ValidationError("请先注册账号.")
        if not get_user_model().objects.filter(username=username).first().is_active:
            raise ValidationError("请先激活账号.")
        return self.cleaned_data


class RegisterForm(UserCreationForm):
    """注册表单类"""

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "username", "class": "form-control"})
        self.fields['email'].widget = widgets.EmailInput(attrs={'placeholder': "email", "class": "form-control"})
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={'placeholder': "repeat password", "class": "form-control"})

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("该邮箱已经存在.")
        return email

    class Meta:
        model = get_user_model()
        fields = ("username", "email")

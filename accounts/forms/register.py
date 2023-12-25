from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password

from phonenumber_field.formfields import PhoneNumberField

from accounts.models import User


class RegisterForm(forms.ModelForm):
    phone = PhoneNumberField(region='IR', label=_("شماره همراه"))
    password = forms.CharField(
        required=True,
        label=_("رمز عبور"),
        widget=forms.PasswordInput(),
        validators=[validate_password]
    )
    password2 = forms.CharField(
        required=True,
        label=_("تکرار رمز عبور"),
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(label=_("ایمیل"), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'field'
            })

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'password', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.object.filter(username=username)
        if user:
            raise ValidationError(_("این نام کاربری از قبل وجود دارد"))
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.object.filter(email=email)
        if user:
            raise ValidationError(_("این ایمیل از قبل وجود دارد"))
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = User.object.filter(phone=phone)
        if user:
            raise ValidationError(_("این شماره همراه از قبل وجود دارد"))
        return phone

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p2 != p1:
            raise ValidationError(_("رمز های عبور باید باهم برابر باشند"))

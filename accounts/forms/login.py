from django import forms
from django.utils.translation import gettext_lazy as _


class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'field'
            })

    phone = forms.CharField(label=_("شماره همراه"), widget=forms.TextInput())
    password = forms.CharField(label=_("رمز عبور"), widget=forms.PasswordInput())

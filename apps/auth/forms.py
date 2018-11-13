from django import forms
from django.contrib.auth.password_validation import CommonPasswordValidator

class ChangePasswordForm(forms.Form):
    password = forms.CharField(label='密碼', max_length=50, widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        validator = CommonPasswordValidator()
        validator.validate(password)
        return password

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    @property
    def errors_prettified(self) -> str:
        errors_list = []
        for field, errors in self.errors.get_json_data().items():
            field_errors = [error["message"] for error in errors]
            errors_list.append(f'{field} - {", ".join(field_errors)}')
        return '\n'.join(errors_list)


class RegisterForm(forms.ModelForm):
    phone_number = forms.CharField(label='Phone number')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    @property
    def errors_prettified(self) -> str:
        errors_list = []
        for field, errors in self.errors.get_json_data().items():
            field_errors = [error["message"] for error in errors]
            errors_list.append(f'{field} - {", ".join(field_errors)}')
        return '\n'.join(errors_list)

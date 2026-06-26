from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User

        field = [
            'username',
            'email',
            'profile_pic',
            'user_type',
            'password'
        ]
    
    def clean(self):
        username = self.cleaned_data.get('username')

        if len(username) < 3:
            raise forms.ValidationError(
                'Username must be at least greater than 3 character'
            )
        return username
    
    def clean(self):
        email = self.cleaned_data.get('email')

        if "@" and "." not in email:
            raise forms.ValidationError(
                'Invalid email, try again with correct email address'
            )
        return email
    
    def clean(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError(
                'Password must be at least greater than 3 character'
            )
        return password

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
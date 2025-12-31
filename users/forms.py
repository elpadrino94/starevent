from django import forms
from users.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'phone_number', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
        }




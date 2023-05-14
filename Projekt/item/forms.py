from django import forms
from .models

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Username',
    'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
    'placeholder': 'Email',
    'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat password',
    'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    'placeholder': 'Username',
    'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Password',
    'class': 'w-full py-4 px-6 rounded-xl'
    }))
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.forms import ModelForm 
from django import forms 
from .models import Profile, Post, Comment

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'class': 'form-control'}))
	middle_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(max_length=254, widget = forms.TextInput(attrs={'class': 'form-control'}))
	gender=forms.ChoiceField(choices=[('M','Male'),('F','Female')])
	birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), help_text='Required. Format: YYYY-MM-DD', )

	class Meta:
		model = User 
		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
		fields = ['first_name', 'last_name', 'middle_name', 'username', 'email', 'gender', 'birth_date', 'password1', 'password2',]


class PostForm(ModelForm):
	publish = forms.CharField(widget = forms.HiddenInput(attrs={'id': 'publish', 'value': 0}))
	class Meta:
		model = Post
		widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class':'form-control',}),
            'body': forms.Textarea(
                attrs={'placeholder': 'Enter contents here!', 'class':'form-control', }),
        }
		fields = ['title', 'body', 'publish']

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		widgets = {'body': forms.Textarea(attrs={'placeholder': 'Enter comment', 'class':'form-control'}),}
		fields = ['body',]
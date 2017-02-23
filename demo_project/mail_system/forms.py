from django import forms
from mail_system.models import Mail, RegisteredUsers
from django.contrib.auth.models import User 

class UserForm(forms.ModelForm):
	password = forms.CharField(label="",widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}))
	username = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Username'}))
	email = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Email'}))	
	class Meta:
		model = User	
		fields = ('username','email','password')

class RegisteredUsersForm(forms.ModelForm):
	mobile = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'Mobile'}))
	city = forms.CharField(label="",widget = forms.TextInput(attrs = {'placeholder': 'City'}))
	class Meta:
		model = RegisteredUsers
		fields = ('mobile','city')

class MailForm(forms.ModelForm):
    class Meta:
    	model = Mail
    	fields = ('content','subject')	

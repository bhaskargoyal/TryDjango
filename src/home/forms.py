from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	name = forms.CharField()
	message = forms.CharField()

	# put some validatioons here

class SignUpForm(forms.ModelForm):
	class Meta():
		model = SignUp
		fields = ['name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username, company = email.split('@')
		domain, extension = company.split('.')
		print extension
		if extension != "com":
			raise forms.ValidationError("Not a valid .com address")
		return email

	def clean_name(self):
		name = self.cleaned_data.get('name')
		return name

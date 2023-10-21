from django import forms
from .models import ContactProfile, Booking


class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Your name',
			'id': 'name',
			'class': 'form-control',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your email',
			'id': 'email',
			'class': 'form-control',
			}))
	subject = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Subject',
			'id': 'subject',
			'class': 'form-control',
			}))	
	message = forms.CharField(max_length=1000, required=False, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Your message',
			'id': 'message',
			'class': 'form-control',
			'rows': 5,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'subject', 'message',)


class BookingForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Your name',
			'class': 'form-control',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Your email',
			'class': 'form-control',
			}))
	phone = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Phone',
			'class': 'form-control',
			}))
	date = forms.DateField(
		widget=forms.DateInput(attrs={
			'placeholder': 'Date',
			'class': 'form-control',
			}))
	time = forms.TimeField(
			widget=forms.TimeInput(attrs={
			'placeholder': 'Time',
			'class': 'form-control',
			}))
	people = forms.IntegerField(required=True, min_value=1,
		widget=forms.NumberInput(attrs={
			'placeholder': '# of people',
			'class': 'form-control',
			}))		
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Your message',
			'class': 'form-control',
			'rows': 5,
			}))
	

	class Meta:
		model = Booking
		fields = ('name', 'email', 'phone', 'date', 'time', 'people', 'message',)
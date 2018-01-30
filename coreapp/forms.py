from django.forms import ModelForm
from .models import Patient, Specimen, Laboratory, LabResult
from django import forms
import datetime
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField


class PatientSearchForm(forms.Form):

	first_name = forms.CharField()
	mobile = PhoneNumberField()
	member_id = forms.IntegerField(help_text='insurance member id', required=False)
	

class PatientRegistrationForm(ModelForm):

	class Meta:
		model = Patient
		fields = '__all__'

class LabTestRequestForm(forms.Form):

	specimens = Specimen.objects.all()
	labs = Laboratory.objects.all()
	date = forms.DateField(initial=datetime.date.today)
	# test_duration = forms.IntegerField(min_value=0, help_text="approximate duration (hrs)")
	lab = forms.ModelChoiceField(queryset=labs, empty_label="(select)", required=False)
	specimen = forms.ModelChoiceField(queryset=specimens, empty_label="(select)")


# login 

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields =('username', 'email', 'password')


class LabResultForm(ModelForm):

	class Meta:
		model = LabResult
		fields = ['test_result', 'diagnosis', 'lab' ]




from django.forms import ModelForm
from .models import Patient, Specimen, Laboratory, LabResult
from django import forms
import datetime
from django.contrib.auth.models import User


class PatientSearchForm(ModelForm):

	class Meta:
		model = Patient
		fields = ['first_name', 'mobile', 'member_id']


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
		fields = '__all__'

		
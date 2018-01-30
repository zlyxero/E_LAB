from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.


class Insurance(models.Model):
	""" Records Insurance companies that the hospital supports/allows transactions with."""

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'insurance'


class LabTest(models.Model):
	""" Records lab tests that can be conducted """

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Laboratory(models.Model):
	""" Records laboratory names where lab test requests can be sent to """		

	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'laboratories'

	def __str__(self):
		return self.name	

class Specimen(models.Model):
	""" Records specimen that accompany lab test requests """

	name = models.CharField(max_length=100)	

	def __str__(self):
		return self.name

class Patient(models.Model):
	""" Patient details"""

	first_name = models.CharField(max_length=35, verbose_name='first name')
	last_name = models.CharField(max_length=35)
	middle_name = models.CharField(max_length=35)
	email = models.EmailField()
	mobile = PhoneNumberField(unique=True)
	date_of_birth = models.DateField()
	member_id = models.IntegerField(verbose_name='insurance member id', blank=True)

	insurance = models.ForeignKey(Insurance, models.SET_NULL, null=True, verbose_name='insurance company', blank=True)

	def __str__(self):
		return "{} {} ".format(self.first_name, self.last_name)

class LabRequest(models.Model):
	""" Records of lab requests made """

	lab_test = models.ManyToManyField(LabTest) 
	patient = models.ForeignKey(Patient, models.PROTECT)
	date = models.DateTimeField(auto_now=True)
	lab = models.ForeignKey(Laboratory, models.PROTECT, null=True)


	def __str__(self):
		return "{} request for patient by name {} {}".format(self.lab_test, self.patient.first_name, self.patient.middle_name)   

class LabResult(models.Model):
	""" Records Lab results - not viewed yet and updated by a doctor """

	lab_request = models.OneToOneField(LabRequest, models.CASCADE) # the test conducted
	diagnosis = models.TextField(null=False, blank=False)
	date = models.DateField(auto_now_add=True) # date when the result was recorded
	lab = models.ForeignKey(Laboratory, models.PROTECT)
	test_result = models.TextField(null=False, blank=False)

	def __str__(self):
		return '[possible diagnosis]: ' + self.diagnosis

class LabResultUpdated(models.Model):
	""" Records viewed and updated lab results, by the doctor """

	lab_request = models.ForeignKey(LabRequest, models.PROTECT)
	diagnosis = models.TextField(null=False, blank=False)
	visit_type = models.CharField(max_length=15)
	date = models.DateField(auto_now_add=True)
	lab = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'lab results updated'


	def __str__(self):
		return 'diagnosis: ' + self.diagnosis	


class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User, models.PROTECT)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)

	def __str__(self):
		return self.user.username					

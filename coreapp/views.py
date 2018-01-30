from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, UpdateView
from .forms import PatientSearchForm, LabTestRequestForm, PatientRegistrationForm, LabResultForm
from . import models
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy 


# Create your views here.

class SearchPatient(View):

	def get(self, request):

		form = PatientSearchForm()
		return render(request, 'coreapp/patient_search_form.html', {'form': form})

	def post(self, request):
		
		form = PatientSearchForm(request.POST)

		if form.is_valid():

			first_name = form.cleaned_data['first_name']
			mobile = form.cleaned_data.get('mobile')
			member_id = form.cleaned_data.get('member_id')

			if mobile:
				query_set = models.Patient.objects.filter(first_name__iexact=first_name, mobile=mobile)

			elif member_id:
				query_set = models.Patient.objects.filter(first_name=first_name, mobile=mobile)

			else:
				query_set = models.Patient.objects.filter(first_name__iexact=first_name)
			
			return render(request, 'coreapp/patient_search_results.html', {'query_set': query_set})

		
		else:
			return render(request, 'coreapp/patient_search_form.html', {'form': form})



class PatientRegistration(View):

	def get(self, request):

		form = PatientRegistrationForm()
		
		return render(request, 'coreapp/patient_registration_form.html', {'form': form})

	def post(self, request):
		
		form = PatientRegistrationForm(request.POST)

		if form.is_valid():
			mobile = form.cleaned_data['mobile']
			last_name = form.cleaned_data['last_name']
			form.save()

			patient = models.Patient.objects.get(mobile=mobile, last_name=last_name)

			return redirect('coreapp:lab-test-request', patient_id=patient.id)


class LabTestRequest(View):

	def get(self, request, patient_id):

		# get patient
		patient = models.Patient.objects.get(id=patient_id)
		form = LabTestRequestForm()
		return render(request, 'coreapp/lab_test_request_form.html', {'form': form, 'patient': patient})

	def post(self, request, patient_id):
		
		# Instantiate form with form data recienved
		form = LabTestRequestForm(request.POST)
		
		# get patient
		patient = models.Patient.objects.get(id=patient_id)

		if form.is_valid():

			# get form values
			lab = form.cleaned_data.get('lab', '')
			specimen = form.cleaned_data['specimen']
			date = form.cleaned_data['date']

			# create a new lab request object instance with above data


			lab_request_object = models.LabRequest(

						patient = patient,
						date = date,
						lab = lab,
					)

			# # save lab request object before adding tests 
			lab_request_object.save()

			# get selected tests (strings)
			test_list = request.POST.getlist('test')

			# get tests object from DB and save it in a list called lab_test_objects
			lab_test_objects = []
			for test in test_list:
				test_object = models.LabTest.objects.get(name__iexact=test)
				lab_test_objects.append(test_object)

			# associate given lab test objects with our lab_request_object
			lab_request_object.lab_test.set(lab_test_objects) 

			return redirect('coreapp:lab-request-submitted', patient_id=patient_id )	

		return render(request, 'coreapp/lab_test_request_form.html', {'form': form, 'patient': patient})
		

def lab_request_success(request, patient_id):
	
	""" lets the doctor know that the lab request made was submitted successfully"""
	patient = models.Patient.objects.get(id=patient_id)
	
	return render(request, 'coreapp/lab_request_success.html', {'patient':patient})


		

def autocomplete(request):

    if request.is_ajax():
        queryset = models.LabTest.objects.filter(name__istartswith=request.GET.get('search', None))
        
        list = []        
        for i in queryset:
            list.append(i.name)
        data = {
            'list': list,
        }
        
        return JsonResponse(data)


def testvalue(request):



    if request.is_ajax():

        # attempt to fetch value from database
        test = models.LabTest.objects.get(name__iexact=request.GET.get('test', None))
        
        # if there is a test value, assign exists the value of 1 else assign it 0
        if test:
           exists = 1
        else:
           exists = 0

        data = {'exists': exists}

        return JsonResponse(data)		



def LabRequestsList(request):
	
	labrequest_list = models.LabRequest.objects.all()
	
	context = {'labrequest_list': labrequest_list}

	return render(request, 'coreapp/labrequest_list.html', context)

def LabRequestDetail(request, request_id):

	labrequest = models.LabRequest.objects.get(id=request_id)
	labtests = labrequest.lab_test.all()

	context = {'request': labrequest, 'labtests':labtests}
	
	return render(request, 'coreapp/labrequest_detail.html', context)



def user_login(request):

	# If the request is a HTTP POST, try to pull out the relevant info.
	errors = False
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form

		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password
		# combination is valid - a User object is returned if it is.

		user = authenticate(username= username, password=password)

		# If we have a user object, the details are correct.
		# If None, no user with matching credentials was found.
		if user is not None:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return redirect('coreapp:search-patient')
			else:
				# An inactive account was used -- no logging in!
				return HttpResponse("Your E-lab account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {}, {}".format(username, password))
			errors = True

	
	return render(request, 'coreapp/login.html', {'errors':errors})			


class LabResult(View):
	""" form used to add a result for a requested lab test """
	def get(self, request, request_id):

		form = LabResultForm()	
		return render(request, 'coreapp/lab_result_form.html', {'form':form})

	def post(self, request, request_id):

		form = LabResultForm(request.POST)

		if form.is_valid():

			diagnosis = form.cleaned_data['diagnosis']
			lab = form.cleaned_data['lab']
			test_result = form.cleaned_data['lab']

			lab_request = get_object_or_404(models.LabRequest, id=request_id)
			
			# create a new lab result object and save

			result = models.LabResult(
					diagnosis = diagnosis,
					lab = lab,
					test_result = test_result,
					lab_request = lab_request

				)

			result.save()

			return redirect('coreapp:lab-result-success')
		
		else:
			return render(request, 'coreapp/lab_result_form.html', {'form':form})


def LabResultDetail(request, result_id):
	
	""" The details of a lab result. From the url we get the id of of a lab result """
	
	lab_result = get_object_or_404(models.LabResult, id=result_id)
	lab_request = lab_result.lab_request

	# get labtests associated with our lab request 
	labtests = lab_request.lab_test.all()

	context = {'lab_result': lab_result, 'lab_request': lab_request, 'labtests':labtests}

	return render(request, 'coreapp/lab_result_detail.html', context)


class LabResultUpdate(UpdateView):

	""" Update lab results """

	model = models.LabResult
	fields = ['diagnosis']
	template_name = 'coreapp/labresult_update_form.html'
	success_url = reverse_lazy('coreapp:labresult-updated')


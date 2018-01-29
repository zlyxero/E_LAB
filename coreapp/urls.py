from django.urls import path, re_path
from . import views


app_name = 'coreapp'

urlpatterns = [
    path('search-patient/', views.SearchPatient.as_view(), name='search-patient'),
    path('patient-registration/', views.PatientRegistration.as_view(), name='patient-registration'),
    re_path('(?P<patient_id>[\d]+)/make-lab-request/', views.LabTestRequest.as_view(), name='lab-test-request'),
    path('ajax/autocomplete/', views.autocomplete, name='ajax_autocomplete'),
    path('ajax/testvalue/', views.testvalue, name='ajax_testvalue'),
    path('(?P<patient_id>[\d]+)/lab-request-submitted/', views.lab_request_success, name='lab-request-submitted'),
    path('lab-request-list/', views.LabRequestsList, name='lab-request-list'),
    re_path('(?P<request_id>[\d]+)/lab-request-detail/', views.LabRequestDetail, name='lab-request-detail'),

]

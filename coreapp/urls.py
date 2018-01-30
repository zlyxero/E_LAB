from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


app_name = 'coreapp'

urlpatterns = [

    path('search-patient/', views.SearchPatient.as_view(), name='search-patient'),
    path('patient-registration/', views.PatientRegistration.as_view(), name='patient-registration'),

    re_path('(?P<patient_id>[\d]+)/make-lab-request/', views.LabTestRequest.as_view(), name='lab-test-request'),
    path('ajax/autocomplete/', views.autocomplete, name='ajax_autocomplete'),
    path('ajax/testvalue/', views.testvalue, name='ajax_testvalue'),
    re_path('(?P<patient_id>[\d]+)/lab-request-submitted/', views.lab_request_success, name='lab-request-submitted'),

    path('lab-request-list/', views.LabRequestsList, name='lab-request-list'),
    re_path('lab-request/(?P<request_id>[\d]+)/', views.LabRequestDetail, name='lab-request-detail'),

    re_path('add-labresult/request/(?P<request_id>[\d]+)/', views.LabResult.as_view(), name='new-lab-result'),
    path('labresult/submit-success/', TemplateView.as_view(template_name='coreapp/lab_result_success.html'), name='lab-result-success'),
    re_path('labtest/results/(?P<result_id>[\d]+)/', views.LabResultDetail, name='lab-test-result'),
    re_path('labresult/(?P<pk>\d+)/update/', views.LabResultUpdate.as_view(), name='lab-result-update'),
    path('labresult/update-success', TemplateView.as_view(template_name='coreapp/labresult_update_success.html'), name='labresult-updated')

]

from django.test import TestCase
from .models import Patient
# Create your tests here.

class PatientModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):

		# Set up data for the Test Case
		Patient.objects.create(
				first_name = 'Brenda',
				last_name = 'Moraa',
				middle_name = 'Bribri',
				email = 'brendamoraa@yahoo.com',
				mobile = '+254700111222',
				date_of_birth = '1994-10-20',
				insurance = 'AAR',
				member_id = 31723789
			)

		def test_object_content(self):
			"""  test data in a sample patient field """

			patient = Patient.object.get(id=1)
			expected_object_last_name = patient.last_name
			self.assertEquals(expected_object_last_name, 'Moraa') 

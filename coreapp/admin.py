from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Insurance)
admin.site.register(models.LabTest)
admin.site.register(models.Laboratory)
admin.site.register(models.Specimen)
admin.site.register(models.Patient)
admin.site.register(models.LabRequest)
admin.site.register(models.LabResult)
admin.site.register(models.LabResultUpdated)
from django.contrib import admin

from main.models import InspectionUpload


class InspectionUploadAdmin(admin.ModelAdmin):
    model = InspectionUpload
    list_display = ('id', 'agent_email', 'inspection_file')

admin.site.register(InspectionUpload, InspectionUploadAdmin)


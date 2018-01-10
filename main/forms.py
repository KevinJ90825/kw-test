from django import forms

from main.models import InspectionUpload


class InspectionUploadForm(forms.ModelForm):

    class Meta(object):
        model = InspectionUpload
        fields = ['inspection_file', 'agent_email']

        widgets = {
            'inspection_file': forms.FileInput(attrs={'class': 'dropify', 'multiple': True}),
            'agent_email': forms.TextInput(attrs={'class': 'form-control'})
        }
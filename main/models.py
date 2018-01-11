from django.db import models
import os

def get_upload_path(instance, filename):
    return os.path.join(instance.agent_email.lower(), filename)

class InspectionUpload(models.Model):

    agent_email = models.EmailField()
    inspection_file = models.FileField(upload_to=get_upload_path)


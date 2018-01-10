from django.db import models
import os

def get_upload_path(instance, filename):
    return os.path.join(str(instance.agent_email.split('@')[0]), filename)

class InspectionUpload(models.Model):

    agent_email = models.EmailField()
    inspection_file = models.FileField(upload_to=get_upload_path)


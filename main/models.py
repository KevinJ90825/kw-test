from django.contrib.postgres.fields import JSONField
from django.db import models

class HomeBuyer(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()

    email = models.EmailField()

    agent_email = models.EmailField(null=True)

    current_address = models.TextField()
    property_address = models.TextField()

    housecanary = JSONField(null=True)

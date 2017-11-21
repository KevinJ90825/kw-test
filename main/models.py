from django.db import models

class HomeBuyer(models.Object):

    first_name = models.TextField()
    last_name = models.TextField()

    email = models.EmailField()

    current_address = models.TextField()
    property_address = models.TextField()

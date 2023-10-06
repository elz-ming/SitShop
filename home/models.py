from django.db import models

###from medium.com add the imports
from django.shortcuts import reverse

from core import settings


###

# Create your models here.
# declare a new model with a name "GeeksModel"
class YourModel(models.Model):
    your_field = models.CharField(max_length=100)
    # Add more fields as needed for your specific model
    # In this example, YourModel is a Django model with a single field named your_field.
    def __str__(self):

        return self.your_field



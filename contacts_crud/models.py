import uuid
from django.db import models

# Create your models here.
class Contact(models.Model):
    """A contact of the user"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)  # Mandatory
    mobile_no = models.CharField(max_length=15, blank=False, null=False)  # Mandatory
    address = models.CharField(max_length=200, blank=True, null=True)  # Optional
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representing the contact."""
        return self.name  # Fixed return value to represent the object properly
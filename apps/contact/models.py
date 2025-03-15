from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    """
    Contact model for storing user inquiries.
    """

    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(db_index=True, unique=True, max_length=150)
    phone_number = models.CharField(max_length=20, db_index=True, unique=True)
    subject = models.CharField(max_length=255)
    message = RichTextField(null=True, blank=True)

    class Meta:
        """
        Meta class for Contact model.
        """

        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        """
        String representation of Contact model.
        """

        return f"{self.name} - {self.subject}"

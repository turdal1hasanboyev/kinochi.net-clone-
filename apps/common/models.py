from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in the application.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        """
        Meta class for the application's base model.
        """

        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'


class SubEmail(BaseModel):
    """
    Model for sub email.
    """

    sub_email = models.EmailField(
        unique=True, db_index=True, null=True, blank=True, max_length=50)

    class Meta:
        """
        Meta class for the sub email model.
        """

        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'

    def __str__(self):
        """
        String representation of the sub email model.
        """

        return f"{self.sub_email}"

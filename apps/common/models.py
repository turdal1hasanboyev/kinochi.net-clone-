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

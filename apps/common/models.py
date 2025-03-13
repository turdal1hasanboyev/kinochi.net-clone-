from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'


class SubEmail(BaseModel):
    sub_email = models.EmailField(unique=True, db_index=True, null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = 'Sub Email'
        verbose_name_plural = 'Sub Emails'
    
    def __str__(self):
        return f"{self.sub_email}"

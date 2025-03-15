from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Contact Admin Model
    """

    model = Contact
    ordering = ('-id',)
    list_display = (
        'id',
        'name',
        'email',
        'phone_number',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
        'email',
        'phone_number',
    )
    list_filter = (
        'is_active',
        'subject',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "email", "phone_number", "subject", "message", "is_active",),
        }),
        ("Metadata", {
            "fields": ("id", "created_at", "updated_at",),
        }),
    )

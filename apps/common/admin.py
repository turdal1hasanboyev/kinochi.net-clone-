from django.contrib import admin

from .models import SubEmail


admin.site.site_header = "Kinochi Admin Panel"
admin.site.site_title = "Kinochi Admin Panel"
admin.site.index_title = "Welcome to Kinochi Admin Panel!"


@admin.register(SubEmail)
class SubEmailAdmin(admin.ModelAdmin):
    ordering = (
        '-id',
    )
    list_display = (
        'id',
        'sub_email',
        'is_active',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'sub_email',
    )
    list_filter = (
        'is_active',
    )

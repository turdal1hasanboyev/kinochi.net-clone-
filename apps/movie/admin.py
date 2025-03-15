from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Movie Admin Model
    """

    model = Movie
    ordering = ('id',)
    list_display = (
        'id',
        'name',
        'slug',
        'category',
        'views',
        'image',
        'premiere_date',
        'author',
        'from_the_movie',
        'trailer',
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_active',
        'category',
        'author',
    )
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('name',)
    }

    fieldsets = (
    ('Basic Information', {
        'fields': ('name', 'slug', 'category', 'tags', 'author', 'from_the_movie', 'description',)
    }),
    ('Image and Trailer', {
        'fields': ('image', 'trailer',),
    }),
    ('Additional Information', {
        'fields': ('views', 'premiere_date', 'is_active',),
    }),
    ('System Information', {
        'fields': ('created_at', 'updated_at', 'id',),
    }),
    )

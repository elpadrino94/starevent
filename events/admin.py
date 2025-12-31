from django.contrib import admin

from events.models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'start_datetime', 'status', 'promoter')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'category', 'city')
    search_fields = ('title', 'description', 'city')

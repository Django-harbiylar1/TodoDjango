from django.contrib import admin
from todo.models import Category, Todo

# Register your models here.


# admin.site.register(Category)
# admin.site.register(Todo)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active']
    search_fields = ['name']
    ordering = ['-created_at']


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at', 'updated_at', 'category__name']
    list_filter = ['is_completed']
    search_fields = ['title', 'description']
    ordering = ['-created_at']

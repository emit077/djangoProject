from django.contrib import admin

from .models import TestUser


@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "mobile", "address", "pincode", "created", "modified"]
    search_fields = ["name", "email", "mobile"]
    list_filter = ['created', 'modified']

from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
        model = Service

        def has_add_permission(self, request):
                return False


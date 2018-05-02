from django.contrib import admin
from .models import ActivitiesDescription


@admin.register(ActivitiesDescription)
class ActivitiesDescriptionAdmin(admin.ModelAdmin):
        model = ActivitiesDescription

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
            return False


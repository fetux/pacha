from django.contrib import admin
from .models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
        model = AboutUs

        def has_add_permission(self, request):
                return False

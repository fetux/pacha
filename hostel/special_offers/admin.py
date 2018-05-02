from django.contrib import admin

from django.contrib import admin
from .models import SpecialOffer


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
        model = SpecialOffer

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
                return False
from django.contrib import admin
from .models import CruiseShip, CruiseShipItinerary, Deal


@admin.register(CruiseShip)
class CruiseShipAdmin(admin.ModelAdmin):
    model = CruiseShip


@admin.register(CruiseShipItinerary)
class CruiseShipItineraryAdmin(admin.ModelAdmin):
    model = CruiseShipItinerary


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    model = Deal

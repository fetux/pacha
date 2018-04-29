from django.db import models


class CruiseShip(models.Model):

    TOURIST_CLASS = 'TC'
    TOURIST_SUPERIOR_CLASS = 'TS'
    FIRST_CLASS = 'FC'

    CRUISE_SHIP_CATEGORIES = (
        (TOURIST_CLASS, 'Tourist Class'),
        (TOURIST_SUPERIOR_CLASS, 'Tourist Superior Class'),
        (FIRST_CLASS, 'First Class')
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=2, choices=CRUISE_SHIP_CATEGORIES)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cruise Ship'
        verbose_name_plural = 'Cruise Ships'


class CruiseShipItinerary(models.Model):

    name = models.CharField(max_length=255)
    cruise_ship = models.ForeignKey(CruiseShip, on_delete=models.CASCADE)
    description = models.TextField()
    included = models.TextField()
    not_included = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cruise Ship Itinerary'
        verbose_name_plural = 'Cruise Ships Itineraries'


class Deal(models.Model):

    cruise_ship = models.ForeignKey(CruiseShip, on_delete=models.CASCADE)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    regular_price = models.FloatField()
    last_minute_price = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} {}".format(self.cruise_ship, self.departure_date, self.arrival_date)

    class Meta:
        verbose_name = 'Galapagos Deal'
        verbose_name_plural = 'Galapagos Deals'


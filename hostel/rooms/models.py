from django.db import models


class Room(models.Model):

    room = models.CharField(max_length=40)
    description = models.TextField(null=True, blank=True)
    price_shared = models.FloatField()
    price_private = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.room

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'


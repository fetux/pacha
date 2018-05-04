from django.db import models


class CarouselImage(models.Model):

    image = models.ImageField()
    active = models.BooleanField(default=True)

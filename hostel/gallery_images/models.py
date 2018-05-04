from django.db import models


class GalleryImage(models.Model):

    image = models.ImageField()
    category = models.CharField(max_length=3)

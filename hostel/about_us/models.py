from django.db import models


class AboutUs(models.Model):

    video_url = models.URLField()
    text = models.TextField()

    def __str__(self):
        return "El Hostel"

    class Meta:
        verbose_name = 'El Hostel'
        verbose_name_plural = 'El Hostel'

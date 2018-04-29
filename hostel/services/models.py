from django.db import models


class Service(models.Model):

    title = models.CharField(max_length=40)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

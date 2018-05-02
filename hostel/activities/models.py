from django.db import models
from ckeditor.fields import RichTextField


class ActivitiesDescription(models.Model):

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    def __str__(self):
        return "Activities"

    class Meta:
        verbose_name = 'Activities'
        verbose_name_plural = 'Activities'


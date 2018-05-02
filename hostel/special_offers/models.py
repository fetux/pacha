from django.db import models
from ckeditor.fields import RichTextField


class SpecialOffer(models.Model):

    title = models.CharField(max_length=25)
    text = RichTextField(max_length=70)
    code = models.CharField(max_length=6)

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(max_length=70, verbose_name="Texto")
    code_es = models.CharField(max_length=6, verbose_name="Codigo")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Special Offer'
        verbose_name_plural = 'Special Offers'

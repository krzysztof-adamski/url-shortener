from django.conf import settings
from django.core.validators import URLValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


class Shortcut(models.Model):
    url = models.CharField(max_length=settings.URL_LENGHT, blank=False, null=False, validators=[MaxLengthValidator(settings.URL_LENGHT), URLValidator()])
    link = models.CharField(max_length=100, blank=True, null=False, editable=False)

    class Meta:
        unique_together = [['url', 'link']]

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('shortcut_detail', args=[self.link])

    @property
    def get_link_url(self):
        url = f"{settings.BASE_URL}{self.get_absolute_url()}"
        return url if not url.endswith("/") else url[:-1]

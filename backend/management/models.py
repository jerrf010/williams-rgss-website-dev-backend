from django.db import models
from solo.models import SingletonModel

class SiteSettings(SingletonModel):
    maintainance_mode = models.BooleanField(default=False)
    site_name = models.CharField(default="RGSS STUCO", max_length=50)
    about = models.CharField(default="", max_length=500)


    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

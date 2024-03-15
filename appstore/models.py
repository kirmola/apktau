from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator


class Publisher(models.Model):

    publisher_name = models.CharField(_("Publisher Name"), max_length=100)
    publisher_slug = AutoSlugField(populate_from="publisher_name")

    class Meta:
        verbose_name = _("Publisher")
        verbose_name_plural = _("Publishers")

    def __str__(self):
        return self.publisher_name

    def get_absolute_url(self):
        return reverse("Publisher_detail", kwargs={"pk": self.pk})



class Apps(models.Model):

    app_name = models.CharField(_("App Name"), max_length=100)
    app_package_name = models.CharField(_("Package Name"), max_length=100, unique=True)
    publisher_name = models.ForeignKey("appstore.Publisher", verbose_name=_("Publisher Name"), on_delete=models.CASCADE)
    app_rating = models.IntegerField(_("Rating"), validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    app_downloads = models.BigIntegerField(_("Downloads"), validators = [
        MinValueValidator(0)
    ])
    app_description = models.TextField(_("App Description"))
    app_updated_on = models.DateField(_("Updated On"), auto_now=True)
    app_screenshots = models.JSONField(_("Images"), default=list)
    

    class Meta:
        verbose_name = _("App")
        verbose_name_plural = _("Apps")

    def __str__(self):
        return self.app_name

    def get_absolute_url(self):
        return reverse("App_detail", kwargs={"pk": self.pk})

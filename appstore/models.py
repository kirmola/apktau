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

    CATEGORY = (
        ("app","App"),
        ("game","Game"),
        ("none", "Undefined")
    )

    app_name = models.CharField(_("App Name"), max_length=100)
    app_package_name = models.CharField(_("Package Name"), max_length=100, unique=True)
    publisher_name = models.ForeignKey("appstore.Publisher", verbose_name=_("Publisher Name"), on_delete=models.CASCADE)
    package_category = models.CharField(_("Package Category"), max_length=50, choices=CATEGORY, default=CATEGORY[2])
    app_rating = models.IntegerField(_("Rating"), validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    app_downloads = models.BigIntegerField(_("Downloads"), validators = [
        MinValueValidator(0)
    ])
    app_description = models.TextField(_("App Description"))
    app_updated_on = models.DateField(_("Updated On"), auto_now=True)
    screenshot_1 = models.ImageField(_("Screenshot 1"), upload_to=None, default=None)
    screenshot_2 = models.ImageField(_("Screenshot 2"), upload_to=None, default=None)
    screenshot_3 = models.ImageField(_("Screenshot 3"), upload_to=None, default=None)
    screenshot_4 = models.ImageField(_("Screenshot 4"), upload_to=None, default=None)
    screenshot_5 = models.ImageField(_("Screenshot 5"), upload_to=None, default=None)
    screenshot_6 = models.ImageField(_("Screenshot 6"), upload_to=None, default=None)
    screenshot_7 = models.ImageField(_("Screenshot 7"), upload_to=None, default=None)
    screenshot_8 = models.ImageField(_("Screenshot 8"), upload_to=None, default=None)
    

    class Meta:
        verbose_name = _("App")
        verbose_name_plural = _("Apps")

    def __str__(self):
        return self.app_name

    def get_absolute_url(self):
        return reverse("App_detail", kwargs={"package_id": self.app_package_name})

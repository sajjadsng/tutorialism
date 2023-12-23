from django.db import models
from django.utils.translation import gettext_lazy as _

from category.models import Category


class ShortVideoCategory(Category):
    banner = models.ImageField(
        upload_to='images/short-video-banners/',
        null=True,
        blank=True,
        verbose_name=_("بنر")
    )

    class Meta:
        verbose_name = _("دسته بندی ویدیو های کوتاه")
        verbose_name_plural = _("دسته بندی های ویدیو های کوتاه")

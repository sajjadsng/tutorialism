from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


class Video(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("عنوان")
    )
    description = RichTextUploadingField(verbose_name=_("توضیحات"))
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        allow_unicode=True,
        verbose_name=_("اسلاگ")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name=_("تاریخ ساخت")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name=_("تاریخ آخرین بروزرسانی")
    )

    class Meta:
        abstract = True

    def __str__(self: str) -> str:
        return self.title

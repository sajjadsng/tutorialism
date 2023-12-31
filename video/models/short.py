from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from video.models import Video
from category.models import ShortVideoCategory
from teacher.models import Teacher


class ShortVideo(Video):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='short_videos',
        verbose_name=_("آموزگار")
    )
    video = models.FileField(
        upload_to='videos/shorts/',
        verbose_name=_("ویدیو")
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name=_("قیمت")
    )
    banner = models.ImageField(
        upload_to='images/course-videos/',
        verbose_name=_("بنر")
    )
    categories = models.ManyToManyField(
        ShortVideoCategory,
        related_name='short_videos',
        verbose_name=_("دسته بندی ها")
    )

    class Meta:
        verbose_name = _("ویدیو کوتاه")
        verbose_name_plural = _("ویدیو های کوتاه")
    
    def get_absolute_url(self):
        return reverse (
            'video:short_video_detail',
            kwargs={'video_id': self.id, 'video_slug': self.slug}
        )

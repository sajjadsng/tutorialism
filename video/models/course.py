from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from video.models import Video
from teacher.models import Teacher
from course.models import Course


class CourseVideo(Video):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='course_videos',
        verbose_name=_("آموزگار")
    )
    video = models.FileField(
        upload_to='videos/courses/',
        verbose_name=_("ویدیو")
    )
    courses = models.ManyToManyField(
        Course,
        related_name='videos',
        verbose_name=_("دوره ها")
    )
    banner = models.ImageField(
        upload_to='images/course-videos/',
        verbose_name=_("بنر")
    )

    class Meta:
        verbose_name = _("ویدیو دوره ها")
        verbose_name_plural = _("ویدیو های دوره ها")

    def get_absolute_url(self):
        return reverse(
            "video:course_video",
            kwargs={'video_id': self.id, 'video_slug': self.slug}
        )

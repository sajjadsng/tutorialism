from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import CourseVideo


class CourseVideoView(View):
    def get(self, request, video_id=None, video_slug=None):
        video = get_object_or_404(CourseVideo, id=video_id, slug=video_slug)
        context = {'video': video}
        return render(request, 'video/video.html', context)

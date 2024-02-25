from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

from urllib.parse import unquote

from .models import Course, Comment, User
from video.models import CourseVideo
from .forms import CommentCreateForm
from django.contrib import messages


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        courses_length = len(courses)
        # paginator
        page = request.GET.get('page', 1)
        paginator = Paginator(courses, 8)
        try:
            course_list = paginator.page(page)
        except PageNotAnInteger:
            course_list = paginator.page(1)
        except EmptyPage:
            course_list = paginator.page(paginator.num_pages)

        context = {
            'courses': course_list,
            'courses_length': courses_length
        }
        return render(request, 'course/course_list.html', context)


class CourseDetailView(View):
    form_class= CommentCreateForm

    def setup(self, request, *args, **kwargs):
        self.course_instance = get_object_or_404(Course, pk=kwargs['course_id'], slug=kwargs['course_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # course_slug = unquote(course_slug)
        # course = get_object_or_404(Course, id=course_id, slug=unquote(course_slug))
        comments = Comment.objects.all()
        usernames = User.objects.all()
        introducing_video = CourseVideo.objects.filter(courses=self.course_instance).first()
        videos = CourseVideo.objects.filter(courses=self.course_instance)[1:]

        context = {
            'introducing_video': introducing_video,
            'course': self.course_instance,
            'videos': videos,
            'comments': comments,
            'form':self.form_class,
        }
        return render(request, 'course/course_detail.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.course = self.course_instance
            new_comment.save()
            messages.success(request, 'نظر شما ثبت شد', 'success')
            return redirect('course:course_detail', self.course_instance.id, self.course_instance.slug)


class CourseVideoListView(View):
    def get(self, request, course_id=None, course_slug=None):
        videos = CourseVideo.objects.filter(
            Q(courses__id=course_id) &
            Q(courses__slug=course_slug)
        )
        context = {'videos': videos}
        return render(request, 'course/course_video_list.html', context)


class CourseVideoView(LoginRequiredMixin, View):
    def get(self, request, video_id=None, video_slug=None):
        video = get_object_or_404(CourseVideo, id=video_id, slug=video_slug)
        course_paid = video.courses.filter(sold_to=request.user)

        context = {
            'video': video,
            'course_paid': course_paid
        }
        return render(request, 'course/video_course.html', context)

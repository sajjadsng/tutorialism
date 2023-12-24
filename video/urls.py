from django.urls import path
from .views import CourseVideoView, ShortVideoListView, ShortVideoDetailView

app_name = 'video'
course_urlpatterns = [
    path('<int:video_id>/<str:video_slug>/', CourseVideoView.as_view(), name='course_video'),
]
short_urlpatterns = [
    path('short/', ShortVideoListView.as_view(), name='short_video_list'),
    path('short/<int:video_id>/<str:video_slug>/', ShortVideoDetailView.as_view(), name='short_video_detail'),
]

urlpatterns = course_urlpatterns + short_urlpatterns

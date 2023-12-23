from django.urls import path
from .views import CourseVideoView

app_name = 'video'
urlpatterns = [
    path('<int:video_id>/<str:video_slug>/', CourseVideoView.as_view(), name='course_video'),
]

from django.urls import path
from .views import CourseListView, CourseDetailView, CourseVideoView

app_name = 'course'
urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    path('<int:course_id>/<str:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('video/<int:video_id>/<str:video_slug>/', CourseVideoView.as_view(), name='video_course'),
]

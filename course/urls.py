from django.urls import path
from .views import CourseListView, CourseDetailView

app_name = 'course'
urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    path('<int:course_id>/<str:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
]


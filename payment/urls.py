from django.urls import path
from .views import (
    CartView,
    CartAddCourseView,
    CartRemoveCourseView,
    OrderCreateView,
    OrderDetailView,
)

app_name = 'payment'
cart_course_urlpatterns = [
    path('cart/add/<int:course_id>/', CartAddCourseView.as_view(), name='cart_add_course'),
    path('cart/remove/<int:course_id>/', CartRemoveCourseView.as_view(), name='cart_remove_course'),
]
order_urlpatterns = [
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
]

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_detail'),
] + cart_course_urlpatterns + order_urlpatterns

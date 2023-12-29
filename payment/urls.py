from django.urls import path
from .views import (
    CartView,
    CartAddView,
    CartRemoveView,
    OrderCreateView,
    OrderDetailView,
)


app_name = 'payment'
cart_urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_detail'),
    path('cart/add/<int:course_id>/', CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:course_id>/', CartRemoveView.as_view(), name='cart_remove'),
]
order_urlpatterns = [
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
]

urlpatterns = cart_urlpatterns + order_urlpatterns

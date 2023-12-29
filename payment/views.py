from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .cart import Cart
from course.models import Course
from .models import Order, OrderItem

CART_DETAIL_TEMPLATE = 'payment/cart_detail.html'
CART_DETAIL_URL = 'payment:cart_detail'


class CartView(View):
    """
        Detail of cart values
    """

    def get(self, request):
        cart = Cart(request)
        cart_length = len([i for i in cart])    # length of cart values
        context = {
            'cart': cart,
            'cart_length': cart_length
        }
        return render(request, CART_DETAIL_TEMPLATE, context)


class CartAddView(View):
    def post(self, request, course_id=None):
        cart = Cart(request)
        course = get_object_or_404(Course, id=course_id)
        cart.add(course)
        return redirect(CART_DETAIL_URL)


class CartRemoveView(View):
    def get(self, request, course_id=None):
        cart = Cart(request)
        course = get_object_or_404(Course, id=course_id)
        cart.remove(course)
        return redirect(CART_DETAIL_URL)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id=None):
        order = get_object_or_404(Order, id=order_id)
        context = {'order': order}
        return render(request, CART_DETAIL_TEMPLATE, context)


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total_price())
        for item in cart:
            OrderItem.objects.create(
                order=order,
                course=item['course'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return redirect(CART_DETAIL_URL)

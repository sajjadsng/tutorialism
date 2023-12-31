from django.shortcuts import get_object_or_404, redirect
from django.views import View

from payment.cart import Cart
from course.models import Course

CART_DETAIL_URL = 'payment:cart_detail'


class CartAddCourseView(View):
    def post(self, request, course_id=None):
        cart = Cart(request)
        course = get_object_or_404(Course, id=course_id)
        cart.add(course)
        return redirect(CART_DETAIL_URL)


class CartRemoveCourseView(View):
    def get(self, request, course_id=None):
        cart = Cart(request)
        course = get_object_or_404(Course, id=course_id)
        cart.remove(course)
        return redirect(CART_DETAIL_URL)

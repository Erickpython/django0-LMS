from django.shortcuts import render
from .models import Lesson


# Create your views here.
def lesson_list(request):
    lessons = Lesson.objects.order_by("order")
    return render(request, "courses/lesson_list.html", {"lessons": lessons})
from django.urls import path
from .views import lesson_list

urlpatterns = [
    path("", lesson_list, name="lesson_list"),
]
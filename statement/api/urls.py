from django.urls import path
from .views import *

urlpatterns = [
    path('rest_create_teacher/', TeacherCreateView.as_view()),
    path('rest_all_teacher/', TeacherListView.as_view()),
    path('rest_detail_teacher/<int:pk>/', TeacherDetailView.as_view()),

    path('rest_create_stud/', StudentCreateView.as_view()),
    path('rest_all_stud/', StudentListView.as_view()),
    path('rest_detail_stud/<int:pk>/', StudentDetailView.as_view()),
]


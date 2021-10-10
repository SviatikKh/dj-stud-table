from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('', views.get_all_students, name='students_list'),
    path('create/', StudentCreate.as_view(), name='create_student'),
    path('delete/<int:id>/', views.delete_student_by_id, name='delete_student'),
    path('update/<int:id>', views.student_put, name='update_student'),
    path('clean/', views.delete_all_students, name='delete_all_students'),
]
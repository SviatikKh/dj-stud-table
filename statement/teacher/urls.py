from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('', views.get_all_teachers, name='teacher_list'),
    path('<int:id>/', views.get_by_id, name='get_teacher'),
    path('create/', TeacherCreate.as_view(), name='create'),
    path('delete/<int:id>/', views.delete_teacher_by_id, name='delete_teacher'),
    path('update/<int:id>', views.teacher_put, name='update'),
    path('clean/', views.delete_all_teachers, name='delete_all_teachers'),
]
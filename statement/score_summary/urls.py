from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('', views.show_score_summary, name='score_summary'),
    # path('', views.fill_score_summary, name='score_summary'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/<str:name>/', views.group_detail, name='group_detail')

]

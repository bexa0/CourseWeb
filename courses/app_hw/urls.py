from django.urls import path
from .views import *

urlpatterns = [
    path('', course_list_view, name='course_list'),
    path('detail/<int:pk>/', course_detail_view, name='course_detail'),
    path('create-course/', course_create_view, name='course_create'),
    path('delete-course/', course_delete_view, name='course_delete'),
    path('update-course/<int:pk>', course_update_view, name='course_update'),
    path('module-list/', module_list_view, name='module_list'),
    path('module-detail/<int:pk>/', module_detail_view, name='module_detail'),
    path('create-module/', module_create_view, name='module_create'),
    path('delete-module/', module_delete_view, name='module_delete'),
    path('update-module/<int:pk>', module_update_view, name='module_update'),
    path('lesson-list/', lesson_list_view, name='lesson_list'),
    path('lesson-detail/<int:pk>/', lesson_detail_view, name='lesson_detail'),
    path('create-lesson/', lesson_create_view, name='lesson_create'),
    path('delete-lesson/', lesson_delete_view, name='lesson_delete'),
    path('update-lesson/<int:pk>', lesson_update_view, name='lesson_update'),
]
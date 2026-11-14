from django.urls import path

from .views import (
    teacher_create,
    teacher_delete,
    teacher_detail,
    teacher_edit,
    teacher_list,
)

urlpatterns = [
    path('', teacher_list, name='teacher_list'),
    path('add/', teacher_create, name='teacher_create'),
    path('<int:id>/', teacher_detail, name='teacher_detail'),
    path('<int:id>/edit/', teacher_edit, name='teacher_edit'),
    path('<int:id>/delete/', teacher_delete, name='teacher_delete'),
]

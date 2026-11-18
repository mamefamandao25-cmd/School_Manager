from django.urls import path

from .views import (
    teacher_create,
    teacher_delete,
    teacher_detail,
    teacher_edit,
    teacher_list,
)

app_name = 'teachers'

urlpatterns = [
    path('', teacher_list, name='list'),
    path('add/', teacher_create, name='teacher_create'),
    path('new/', teacher_create, name='create'),
    path('<int:id>/', teacher_detail, name='detail'),
    path('<int:id>/edit/', teacher_edit, name='update'),
    path('<int:id>/edit/', teacher_edit, name='teacher_edit'),
    path('<int:id>/delete/', teacher_delete, name='delete'),
    path('<int:id>/delete/', teacher_delete, name='teacher_delete'),
]

from django.urls import path

from .views import (
    student_create,
    student_delete,
    student_detail,
    student_edit,
    student_list,
    students_by_class,
)

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', student_create, name='student_create'),
    path('<int:id>/', student_detail, name='student_detail'),
    path('<int:id>/edit/', student_edit, name='student_edit'),
    path('<int:id>/delete/', student_delete, name='student_delete'),
    path('classe/<str:classe>/', students_by_class, name='students_by_class'),
]

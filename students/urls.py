from django.urls import path

from .views import (
    student_create,
    student_delete,
    student_detail,
    student_edit,
    student_list,
    students_by_class,
)

app_name = 'students'

urlpatterns = [
    path('', student_list, name='list'),
    path('add/', student_create, name='student_create'),
    path('new/', student_create, name='create'),
    path('<int:id>/', student_detail, name='detail'),
    path('<int:id>/edit/', student_edit, name='update'),
    path('<int:id>/edit/', student_edit, name='student_edit'),
    path('<int:id>/delete/', student_delete, name='delete'),
    path('<int:id>/delete/', student_delete, name='student_delete'),
    path('classe/<str:classe>/', students_by_class, name='by_class'),
]

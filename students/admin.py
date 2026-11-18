from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'classe', 'phone', 'active')
    list_filter = ('classe', 'active')
    search_fields = ('first_name', 'last_name', 'email', 'phone')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject')
    search_fields = ('first_name', 'last_name', 'email', 'subject')

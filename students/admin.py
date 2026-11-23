from django.contrib import admin

from .models import Grade, Student, Subject, Teacher


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'classe', 'phone', 'active')
    list_filter = ('classe', 'active')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    inlines = (GradeInline,)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'title', 'score', 'date')
    list_filter = ('subject', 'date')
    search_fields = ('student__first_name', 'student__last_name', 'subject__name', 'title')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email', 'subjects__name')
    filter_horizontal = ('subjects',)


admin.site.site_header = 'Administration scolaire'
admin.site.site_title = 'School Manager'
admin.site.index_title = 'Gestion de l’établissement'

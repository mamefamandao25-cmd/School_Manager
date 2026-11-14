from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student, Teacher


def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "student_count": Student.objects.count(),
        "active_student_count": Student.objects.filter(active=True).count(),
        "class_count": Student.objects.values("classe").distinct().count(),
        "teacher_count": Teacher.objects.count(),
    }
    return render(request, "students/home.html", context)


def student_list(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.all().order_by("last_name", "first_name")

    if query:
        students = students.filter(
            first_name__icontains=query
        ) | students.filter(
            last_name__icontains=query
        ) | students.filter(
            classe__icontains=query
        )

    context = {
        "students": students.distinct().order_by("last_name", "first_name"),
        "query": query,
    }
    return render(request, "students/student_list.html", context)


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect("student_detail", id=student.id)
    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form, "title": "Ajouter un étudiant"})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "students/student_detail.html", {"student": student})


def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_detail", id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {"form": form, "title": "Modifier un étudiant", "student": student})


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/student_delete.html", {"student": student})


def students_by_class(request, classe):
    students = Student.objects.filter(classe__iexact=classe).order_by("last_name", "first_name")
    return render(request, "students/student_list.html", {"students": students, "query": classe})


def teacher_list(request):
    return render(request, "students/teachers.html", {"teachers": Student.objects.filter(active=True)})


def about(request):
    return render(request, "students/about.html")
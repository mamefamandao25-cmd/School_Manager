from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from students.models import Teacher

from .forms import TeacherForm


def teacher_list(request):
    query = request.GET.get('q', '').strip()
    teachers = Teacher.objects.prefetch_related('subjects').order_by('last_name', 'first_name')

    if query:
        teachers = teachers.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(subjects__name__icontains=query)
        )

    context = {
        'teachers': teachers.distinct().order_by('last_name', 'first_name'),
        'query': query,
    }
    return render(request, 'teachers/teacher_list.html', context)


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            messages.success(request, f"{teacher} a été ajouté(e).")
            return redirect('teachers:list')
    else:
        form = TeacherForm()

    return render(request, 'teachers/teacher_form.html', {'form': form, 'title': 'Ajouter un enseignant'})


def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher.objects.prefetch_related('subjects'), id=id)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})


def teacher_edit(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, f"La fiche de {teacher} a été mise à jour.")
            return redirect('teachers:detail', id=teacher.id)
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'teachers/teacher_form.html', {'form': form, 'title': 'Modifier un enseignant', 'teacher': teacher})


def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        name = str(teacher)
        teacher.delete()
        messages.success(request, f"{name} a été supprimé(e).")
        return redirect('teachers:list')

    return render(request, 'teachers/teacher_delete.html', {'teacher': teacher})

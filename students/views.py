from django.shortcuts import render
from django.http import Http404

# Données temporaires : elles viendront de la base de données plus tard
STUDENTS = [
    {"id": 1, "first_name": "Mame Fama", "last_name": "Ndao", "classe": "L1", "active": True},
    {"id": 2, "first_name": "Moustapha", "last_name": "Ndiaye", "classe": "L2", "active": False},
    {"id": 3, "first_name": "Fatou Binetou", "last_name": "Ladiane", "classe": "L1", "active": False},
    {"id": 4, "first_name": "Khalil", "last_name": "Diaw", "classe": "L3", "active": True},
]
# 1. La page d'accueil
def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Kaffrine",
        "nb_classes": 16,
    }
    return render(request, "students/home.html", context)

# 2. La page de la liste
def student_list(request):
    context = {
        "students": STUDENTS,
    }
    return render(request, "students/student_list.html", context)

# 3. La page détail
def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
            return render(request, "students/student_detail.html", context)
    
    raise Http404("Étudiant introuvable")
# ... (ton code existant au-dessus) ...

def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
            return render(request, "students/student_detail.html", context)
            
    raise Http404("Étudiant introuvable")



# Étape 11 : La page À propos
def about(request):
    return render(request, "students/about.html")

# Étape 12 : Filtrer les étudiants par classe
def students_by_class(request, classe):
    selection = []
    for student in STUDENTS:
        if student["classe"] == classe:
            selection.append(student)
    context = {"students": selection}
    return render(request, "students/student_list.html", context)
TEACHERS = [
    {"first_name": "Mamadou Moustapha", "last_name": "Sarr", "subject": "Mathématiques"},
    {"first_name": "Pape Ibrahima", "last_name": "Niang", "subject": "Informatique"},
    {"first_name": "Cheikh Alssane", "last_name": "Ndoye", "subject": "Anglais"},
]
def teacher_list(request):
    context = {"teachers": TEACHERS}
    return render(request, "teachers.html", context)
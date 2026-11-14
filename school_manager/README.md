# School Manager

## Description
Première application web réalisée avec Django pour consulter des pages liées aux étudiants.

## Prérequis
- Python
- Git
- Django
- Visual Studio Code

## Installation
1. Ouvrir le dossier du projet dans VS Code.
2. Créer et activer un environnement virtuel.
3. Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

## Activation de l'environnement virtuel sous Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

## Lancement du serveur

```bash
python manage.py runserver
```

## URLs disponibles
- Accueil : /
- Liste des étudiants : /students/
- Détail d'un étudiant : /students/15/
- Administration : /admin/
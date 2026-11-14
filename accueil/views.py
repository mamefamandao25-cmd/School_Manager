from django.shortcuts import render


def accueil(request):
    context = {
        'message': 'Bienvenue sur mon site !',
        'author': 'Mame Fama Ndao',
        'study': 'Analyse de Performance Digitale',
    }
    return render(request, 'accueil/accueil.html', context)

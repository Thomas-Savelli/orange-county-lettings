"""
Module de définition des vues pour l'application 'lettings'.

Ce module contient les définitions des vues Django pour l'application 'lettings'.
Il inclut les vues index et letting, qui renvoient respectivement la liste des locations
et les détails d'une location spécifique.
"""

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Letting


def index(request):
    """
    Vue pour afficher la liste des locations.

    Cette vue récupère la liste des locations à l'aide de la fonction get_list_or_404
    et renvoie une réponse rendue à partir du template 'lettings/index.html'.
    """
    lettings_list = get_list_or_404(Letting)
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une location spécifique.

    Cette vue récupère les détails d'une location spécifique à l'aide de la fonction
    get_object_or_404 et renvoie une réponse rendue à partir du template 'lettings/letting.html'.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)

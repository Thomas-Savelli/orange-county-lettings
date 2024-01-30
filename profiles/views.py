"""
Module de définition des vues pour l'application 'profiles'.

Ce module définit les vues pour l'application 'profiles', qui sont responsables de gérer
les requêtes HTTP et de renvoyer les réponses appropriées. Les vues incluent une vue d'index
affichant la liste des profils et une vue de profil individuel affichant les détails d'un
profil spécifique.

Fonctions:
    index: Vue pour afficher la liste des profils.
    profile: Vue pour afficher les détails d'un profil spécifique.
"""

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Profile


def index(request):
    """
    Vue pour afficher la liste des profils.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP.

    Returns:
        HttpResponse: Réponse HTTP contenant la liste des profils rendue dans un template.
    """
    profiles_list = get_list_or_404(Profile)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Vue pour afficher les détails d'un profil spécifique.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP.
        username (str): Nom d'utilisateur du profil.

    Returns:
        HttpResponse: Réponse HTTP contenant les détails du profil rendus dans un template.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)

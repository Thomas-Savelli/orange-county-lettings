"""
Module contenant les vues pour l'application oc_lettings_site.

Ce module définit plusieurs vues, dont la vue principale ('index') et des vues personnalisées
pour la gestion des erreurs 404 et 500. Ces vues utilisent des templates spécifiques pour rendre
les pages associées.
"""

from django.shortcuts import render
from sentry_sdk import capture_message


def index(request):
    """
    Vue pour la page d'accueil 'index'.

    Cette vue rend la page d'accueil en utilisant le template 'index.html'.
    """
    return render(request, 'index.html')


def custom_404(request, *args, **kwargs):
    """
    Vue pour la gestion des erreurs 404.

    Cette vue rend la page d'erreur 404 en utilisant le template '404.html' et
    retourne une réponse avec le statut HTTP 404.
    """
    # Log en cas d'erreur 404
    capture_message("This page was not found !", level='error')
    return render(request, "404.html", status=404)


def custom_500(request, *args, **kwargs):
    """
    Vue pour la gestion des erreurs 500.

    Cette vue rend la page d'erreur 500 en utilisant le template '500.html' et
    retourne une réponse avec le statut HTTP 500.
    """
    # Log en cas d'erreur 500
    capture_message("This page was not found, Error Server !", level='error')
    return render(request, "500.html", status=500)

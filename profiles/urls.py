"""
Module de définition des URLs pour les vues de l'application 'profiles'.

Ce module définit les URLs pour les vues de l'application 'profiles'. Il associe les vues
aux chemins d'URL correspondants, en utilisant les noms d'URL pour référencer les vues.

Variables:
    app_name (str): Nom de l'application utilisé pour créer des espaces de noms d'URL.
    urlpatterns (list): Liste des patterns d'URL associant les vues aux chemins correspondants.
"""

from django.urls import path
from . import views

# Nom de l'application utilisé pour créer des espaces de noms d'URL
app_name = "profiles"

# Liste des patterns d'URL associant les vues aux chemins correspondants
urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]

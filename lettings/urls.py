"""
Module de configuration des URLs pour l'application 'lettings'.

Ce module contient la configuration des URLs pour l'application 'lettings'. Il définit les chemins
d'URLs associés aux vues 'index' et 'letting' dans le module 'views'.
"""

from django.urls import path
from . import views

#  Déclare l'espace de noms (app_name) pour les URLs de l'application lettings
app_name = "lettings"

# Définition des URL patterns de l'application
urlpatterns = [
    path("", views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]

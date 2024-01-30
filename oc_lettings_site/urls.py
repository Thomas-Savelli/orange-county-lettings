"""
Module de configuration des URLS pour l'application oc_lettings_site.

Ce module définit les URL de l'application, y compris les vues, les chemins vers les applications incluses,
et les gestionnaires d'erreurs personnalisés pour les erreurs 404 et 500.
"""

from django.contrib import admin
from django.urls import path, include

from . import views


# Configuration des gestionnaires d'erreurs personnalisés
handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'

# Définition des URL patterns de l'application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('404/', views.custom_404, name='custom_404'),
    path('500/', views.custom_500, name='custom_500')
]

"""
Module de configuration WSGI pour l'application oc_lettings_site.

Ce module configure l'environnement et obtient l'application WSGI de Django pour
permettre le déploiement de l'application avec des serveurs compatibles WSGI.
"""

import os

from django.core.wsgi import get_wsgi_application

# Configuration de l'environnement pour utiliser les paramètres de l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

# Obtention de l'application WSGI de Django
application = get_wsgi_application()

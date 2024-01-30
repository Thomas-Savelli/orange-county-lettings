"""
Module de configuration ASGI pour l'application oc_lettings_site.

Ce module configure l'environnement et obtient l'application ASGI de Django pour
permettre le déploiement de l'application à l'aide d'un serveur ASGI.
"""

import os

from django.core.asgi import get_asgi_application

# Configuration de l'environnement pour utiliser les paramètres de l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

# Obtention de l'application ASGI de Django
application = get_asgi_application()

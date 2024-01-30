"""
Script de gestion Django pour exécuter diverses commandes de gestion du projet.

Ce script utilise le module Django pour exécuter des commandes de gestion du projet, telles que
l'exécution de migrations de base de données, le démarrage du serveur de développement, etc.

Fonctions:
    main: Fonction principale appelée lors de l'exécution du script.
"""

import os
import sys


def main():
    """
    Fonction principale appelée lors de l'exécution du script.

    Configure l'environnement Django et utilise le module Django pour exécuter des commandes
    de gestion du projet à partir de la ligne de commande.

    Raises:
        ImportError: Si Django n'est pas installé ou n'est pas accessible.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

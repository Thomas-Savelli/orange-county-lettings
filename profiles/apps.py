"""
Module de configuration d'application pour l'application 'profiles'.

Ce module définit la configuration d'application pour l'application 'profiles'.
Il spécifie le nom de l'application utilisé dans les paramètres de configuration Django.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration d'application pour l'application 'profiles'.

    Attributes:
        name (str): Nom de l'application utilisé dans les paramètres de configuration Django.
    """
    name = 'profiles'

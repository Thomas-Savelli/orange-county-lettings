"""
Module de définition de modèles pour l'application 'profiles'.

Ce module définit le modèle 'Profile' utilisé pour représenter les profils d'utilisateurs
dans l'application 'profiles'. Chaque profil est associé à un utilisateur unique et peut
inclure des informations supplémentaires telles que la ville préférée.

Classes:
    Profile: Modèle représentant un profil d'utilisateur.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant un profil d'utilisateur.

    Attributes:
        user (User): Champ de liaison OneToOne avec le modèle d'utilisateur de Django.
        favorite_city (str): Champ de texte pour enregistrer la ville préférée de l'utilisateur.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Méthode pour représenter le profil sous forme de chaîne de caractères.

        Returns:
            str: Nom d'utilisateur de l'utilisateur associé au profil.
        """
        return self.user.username

"""
Module de tests unitaires pour le modèle Profile de l'application 'profiles'.

Ce module contient des tests unitaires pour le modèle Profile de l'application 'profiles'.
Il vérifie le comportement des méthodes et attributs du modèle, en mettant l'accent sur
la méthode __str__ qui génère une représentation textuelle du profil.
"""

import pytest
from django.test import Client
from profiles.models import Profile


client = Client()


@pytest.mark.django_db
def test_profile_model(user_1):
    """
    Test unitaire pour le modèle Profile.

    Ce test vérifie que la méthode __str__ du modèle Profile génère la représentation
    attendue pour une instance de profil avec un utilisateur associé.

    Args:
        user_1 (User): Instance du modèle User représentant le premier utilisateur.
    """
    # Crée un profil avec l'utilisateur spécifié et une ville préférée
    profile = Profile.objects.create(user=user_1, favorite_city='Préaulard')
    assert str(profile) == "Harry Potter"

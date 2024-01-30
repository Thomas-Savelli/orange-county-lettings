"""
Module de fixtures pour les tests de l'application 'profiles'.

Ce module contient des fixtures nécessaires pour les tests de l'application 'profiles'.
Il définit des données préparatoires, telles que des utilisateurs et des profils, pour
faciliter la création d'instances nécessaires lors des tests unitaires et d'intégration.
"""

import pytest
from profiles.models import Profile


# Fixture pour l'utilisateur 1
@pytest.fixture
def user_1(django_user_model):
    """
    Fixture pour créer un utilisateur (Harry Potter) à utiliser dans les tests.

    Args:
        django_user_model: Modèle d'utilisateur de Django.

    Returns:
        User: Instance du modèle d'utilisateur pour Harry Potter.
    """
    user = django_user_model.objects.create(
        username='Harry Potter', password='quidditch')
    return user


# Fixture pour l'utilisateur 2
@pytest.fixture
def user_2(django_user_model):
    """
    Fixture pour créer un utilisateur (Ronald Weasley) à utiliser dans les tests.

    Args:
        django_user_model: Modèle d'utilisateur de Django.

    Returns:
        User: Instance du modèle d'utilisateur pour Ronald Weasley.
    """
    user = django_user_model.objects.create(
        username='Ronald Weasley', password='hermoine4ever'
    )
    return user


# Fixture pour le profil de l'utilisateur 1
@pytest.fixture
def profile_1(user_1):
    """
    Fixture pour créer un profil (Préaulard) lié à l'utilisateur 1 pour les tests.

    Args:
        user_1: Instance de l'utilisateur 1.

    Returns:
        Profile: Instance du modèle de profil pour Préaulard.
    """
    profile = Profile.objects.create(user=user_1, favorite_city='Préaulard')
    return profile


# Fixture pour le profil de l'utilisateur 2
@pytest.fixture
def profile_2(user_2):
    """
    Fixture pour créer un profil (Le Terrier) lié à l'utilisateur 2 pour les tests.

    Args:
        user_2: Instance de l'utilisateur 2.

    Returns:
        Profile: Instance du modèle de profil pour Le Terrier.
    """
    profile = Profile.objects.create(user=user_2, favorite_city='Le Terrier')
    return profile

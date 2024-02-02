"""
Module de tests unitaires pour les URLs de l'application 'profiles'.

Ce module contient des tests unitaires pour les URLs de l'application 'profiles'.
Il vérifie que les URLs des pages d'index des profils et des profils individuels
sont correctement configurées et renvoient les bonnes réponses HTTP.

Note: Les tests utilisent des fixtures pour créer
des instances de profils nécessaires : conftest.py
"""

import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from django.test import Client


client = Client()


@pytest.mark.django_db
def test_profiles_index_url(profile_1, profile_2):
    """
    Test unitaire pour l'URL de la vue 'index'.

    Ce test vérifie que l'URL pour la vue 'index' est correctement configurée
    et renvoie la réponse HTTP attendue.

    Args:
        profile_1 (Profile): Instance du modèle Profile représentant le premier profil.
        profile_2 (Profile): Instance du modèle Profile représentant le deuxième profil.
    """

    profile_1
    profile_2

    # Obtiens l'URL à partir de la vue
    url = reverse('profiles:profiles_index')
    # Effectue une requete GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/profiles/'
    assertTemplateUsed(response, 'profiles/index.html')


@pytest.mark.django_db
def test_profiles_profile_url(profile_2):
    """
    Test unitaire pour l'URL de la vue 'profile'.

    Ce test vérifie que l'URL pour la vue 'profile' est correctement configurée
    et renvoie la réponse HTTP attendue.

    Args:
        profile_2 (Profile): Instance du modèle Profile représentant le deuxième profil.
    """

    profile_2

    # Obtiens l'URL à partir de la vue
    url = reverse('profiles:profile', kwargs={"username": 'Ronald Weasley'})

    # Effectue une requete GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/profiles/Ronald%20Weasley/'
    assertTemplateUsed(response, "profiles/profile.html")

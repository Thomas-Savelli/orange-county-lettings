"""
Module de tests unitaires pour les vues de l'application 'profiles'.

Ce module contient des tests unitaires pour les vues de l'application 'profiles'.
Il vérifie que les vues 'index' et 'profile' renvoient les réponses HTTP attendues
et contiennent les informations des profils correctes.

Note: Les tests utilisent des fixtures pour créer des instances de profils nécessaires : conftest.py
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_profiles_index_view(profile_1, profile_2):
    """
    Test unitaire pour la vue 'index'.

    Ce test vérifie que la vue 'index' renvoie la réponse HTTP attendue
    et contient les informations des profils attendues.

    Args:
        profile_1 (Profile): Instance du modèle Profile représentant le premier profil.
        profile_2 (Profile): Instance du modèle Profile représentant le deuxième profil.
    """

    # Crée deux profils en utilisant les fixtures
    profile_1
    profile_2

    # Obtient le chemin de l'URL à partir de la vue
    path = reverse("profiles:profiles_index")

    # Effectue une requête GET
    response = client.get(path)
    content = response.content.decode()

    # Vérifie que les liens vers les profils sont présents dans le contenu
    expected_content_1 = '<a href="/profiles/Harry%20Potter/">Harry Potter</a>'
    expected_content_2 = '<a href="/profiles/Ronald%20Weasley/">Ronald Weasley</a>'

    assert expected_content_1 in content and expected_content_2 in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles_profile_view(profile_2):
    """
    Test unitaire pour la vue 'profile'.

    Ce test vérifie que la vue 'profile' renvoie la réponse HTTP attendue
    et contient les informations du profil attendues.

    Args:
        profile_2 (Profile): Instance du modèle Profile représentant le deuxième profil.
    """

    # Utilise la fixture pour créer un profil
    profile_2

    # Obtient le chemin de l'URL à partir de la vue
    path = reverse("profiles:profile", kwargs={'username': "Ronald Weasley"})

    # Effectue une requête GET
    response = client.get(path)
    content = response.content.decode()

    assert 'Le Terrier' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")

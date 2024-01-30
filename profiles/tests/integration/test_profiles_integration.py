"""
Module de tests d'intégration de l'application 'profiles'.

Ce module contient un test d'intégration qui vérifie le comportement des vues
de l'application 'profiles'. Le test vérifie que les pages d'index des profils
et les pages de profil individuel sont accessibles et contiennent les informations
attendues pour deux profils spécifiques.
"""

import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()


@pytest.mark.django_db
def test_profiles_integration(profile_1, profile_2):
    """
    Test d'intégration pour les vues de l'application 'profiles'.

    Ce test vérifie le comportement des vues de l'application 'profiles'. Il s'assure
    que les pages d'index des profils et les pages de profil individuel sont accessibles
    et contiennent les informations attendues pour deux profils spécifiques.

    Args:
        profile_1 (Profile): Instance du modèle Profile représentant le premier profil.
        profile_2 (Profile): Instance du modèle Profile représentant le deuxième profil.
    """

    # Test de la page d'index des profils
    url = reverse("profiles:profiles_index")
    response = client.get(url)
    content = response.content.decode()

    assert 'Harry Potter' in content
    assert 'Ronald Weasley' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")

    # Test de la page de profil pour le premier utilisateur (Harry Potter)
    url_2 = reverse("profiles:profile", kwargs={"username": "Harry Potter"})
    response = client.get(url_2)
    content = response.content.decode()

    expected_content = profile_1.favorite_city

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")

    # Test de la page de profil pour le deuxième utilisateur (Ronald Weasley)
    url_3 = reverse("profiles:profile", kwargs={"username": "Ronald Weasley"})
    response = client.get(url_3)
    content = response.content.decode()

    expected_content = profile_2.favorite_city

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")

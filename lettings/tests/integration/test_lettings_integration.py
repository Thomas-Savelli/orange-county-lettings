"""
Module de tests d'intégration pour l'application 'lettings'.

Ce module contient des tests d'intégration simulant le parcours utilisateur à travers
les vues de l'application 'lettings'. Il vérifie que les pages sont correctement rendues
avec les informations attendues.
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()


@pytest.mark.django_db
def test_lettings_integration(letting_1, letting_2):
    """
    Test d'intégration pour les vues de l'application 'lettings'.

    Ce test simule le parcours utilisateur à travers les vues de l'application 'lettings'
    et vérifie que les pages sont correctement rendues avec les informations attendues.
    """

    # Préparation des données avec deux objets Letting
    letting_1
    letting_2

    # Recuperation de l'URL a travers lettings_index
    url = reverse("lettings:lettings_index")
    response = client.get(url)
    content = response.content.decode()

    # Récupération de l'URL via la vue 'lettings_index'
    assert "The Burrow" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")

    # Test d'affichage du letting_1 avec l'URL 'letting'
    url_2 = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(url_2)
    content = response.content.decode()

    # Vérification du contenu de la page de détails pour letting_1
    assert "Privet Drive" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")

    # Test d'affichage du letting_2 avec l'URL 'letting'
    url_3 = reverse("lettings:letting", kwargs={"letting_id": 2})
    response = client.get(url_3)
    content = response.content.decode()

    # Vérification du contenu de la page de détails pour letting_2
    assert "Square Grimmaurd" in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")

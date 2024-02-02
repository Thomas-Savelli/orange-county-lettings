"""
Module de tests unitaires pour les URL de l'application 'lettings'.

Ce module contient des tests unitaires pour les URL de l'application 'lettings', y compris
les vues 'index' et 'letting'. Les tests vérifient que les URL renvoient des réponses
HTTP 200 avec les templates appropriés.
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from lettings.models import Letting


# Instanciation du client de test
client = Client()


# Test pour l'URL de la view 'lettings_index'
@pytest.mark.django_db
def test_lettings_index_url(address_1, address_2):
    """
    Test unitaire pour l'URL de la vue 'index' de l'application 'lettings'.

    Ce test crée des instances de modèles Letting et vérifie que l'URL de la vue 'index'
    renvoie une réponse HTTP 200 et utilise le template 'lettings/index.html'.
    """

    # Création d'instances de modèles Letting avec des adresses spécifiques
    Letting.objects.create(title="Harry Potter's House", address=address_1)
    Letting.objects.create(title="The Burrow", address=address_2)

    # Obtiens l'URL à partir de la vue
    url = reverse('lettings:lettings_index')
    # Effectue une requete GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/lettings/'
    assertTemplateUsed(response, "lettings/index.html")


# Test pour l'URL de la view 'letting'
@pytest.mark.django_db
def test_lettings_letting_url(address_2):
    """
    Test unitaire pour l'URL de la vue 'letting' de l'application 'lettings'.

    Ce test crée une instance de modèle Letting et vérifie
    que l'URL de la vue 'letting' avec un ID spécifique renvoie
    une réponse HTTP 200 et utilise le template 'lettings/letting.html'.
    """

    # Création d'une instance de modèle Letting avec une adresse spécifique
    Letting.objects.create(title="The Burrow", address=address_2)

    # Obtiens l'URL à partir de la vue
    url = reverse('lettings:letting', kwargs={"letting_id": 1})
    # Effectue une requete GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/lettings/1/'
    assertTemplateUsed(response, "lettings/letting.html")

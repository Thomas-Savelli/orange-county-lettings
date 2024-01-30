"""
Module de tests unitaires pour les vues de l'application 'lettings'.

Ce module contient des tests unitaires pour les vues 'index' et 'letting' de l'application 'lettings'.
Les tests vérifient que les vues renvoient des réponses HTTP 200 avec les templates appropriés et que le contenu
des pages correspond aux informations attendues.
"""

import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_lettings_index_view(address_1, address_2):
    """
    Test unitaire pour la vue 'index' de l'application 'lettings'.

    Ce test crée des instances de modèles Letting, vérifie que la vue 'lettings_index'
    renvoie une réponse HTTP 200 avec le template 'lettings/index.html' et que le contenu
    de la page inclut les informations attendues.
    """
    # Création d'instances de modèles Letting avec des adresses spécifiques
    Letting.objects.create(title="Harry Potter's House", address=address_1)
    Letting.objects.create(title="The Burrow", address=address_2)

    # Utilisation de reverse() pour obtenir l'URL de la vue 'index'
    path = reverse("lettings:lettings_index")

    # Envoi d'une requête HTTP GET à l'URL obtenu avec reverse()
    response = client.get(path)
    content = response.content.decode()

    # Vérification du contenu de la page d'index
    expected_content = '<a href="/lettings/1/">Harry Potter&#x27;s House</a>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_lettings_letting_view(address_2):
    """
    Test unitaire pour la vue 'letting' de l'application 'lettings'.

    Ce test crée une instance de modèle Letting, vérifie que la vue 'letting' avec un ID spécifique
    renvoie une réponse HTTP 200 avec le template 'lettings/letting.html' et que le contenu
    de la page inclut les informations attendues.
    """
    # Création d'une instance de modèle Letting avec une adresse spécifique
    Letting.objects.create(title="The Burrow", address=address_2)

    # Utilisation de reverse() pour obtenir l'URL de la vue 'letting' avec un ID spécifique
    path = reverse("lettings:letting", kwargs={'letting_id': 1})

    # Envoi d'une requête HTTP GET à l'URL obtenu avec reverse()
    response = client.get(path)
    content = response.content.decode()

    # Vérification du contenu de la page de détails pour Letting
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">The Burrow</h1>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")

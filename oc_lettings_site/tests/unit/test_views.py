"""
Ce module contient les tests unitaires pour les views de l'application oc_lettings_site.

Chaque test vérifie le comportement attendu d'une vue spécifique en utilisant le client de test Django.
Les vues testées incluent 'index', 'custom_404', et 'custom_500'.
"""

import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_index_view():
    """
    Teste la vue 'index'.
    """
    # Utilisation de reverse() pour obtenir l'URL de la vue "index"
    path = reverse("index")
    # Envoi d'une requête HTTP GET à l'URL obtenu avec reverse()
    response = client.get(path)
    content = response.content.decode()

    # Ajustement pour résoudre l'avertissement lié à import cgi
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">' "Welcome to Holiday Homes</h1>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_custom_404_view():
    """
    Teste la vue 'custom_404'.
    """
    # Utilisation de reverse() pour obtenir l'URL de la vue "custom_404"
    path = reverse("custom_404")
    # Envoi d'une requête HTTP GET à l'URL obtenu avec reverse()
    response = client.get(path)
    content = response.content.decode()

    # Ajustement pour résoudre l'avertissement lié à import cgi
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">404 - Page not found</h1>'

    assert expected_content in content
    assert response.status_code == 404
    assertTemplateUsed(response, "404.html")


@pytest.mark.django_db
def test_custom_500_view():
    """
    Teste la vue 'custom_500'.
    """
    # Utilisation de reverse() pour obtenir l'URL de la vue "custom_500"
    path = reverse("custom_500")
    # Envoi d'une requête HTTP GET à l'URL obtenu avec reverse()
    response = client.get(path)
    content = response.content.decode()

    # Ajustement pour résoudre l'avertissement lié à import cgi
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">500 - Server error</h1>'

    assert expected_content in content
    assert response.status_code == 500
    assertTemplateUsed(response, "500.html")

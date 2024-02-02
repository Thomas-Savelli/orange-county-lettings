"""
Ce module contient les tests unitaires pour les
urls de l'application oc_lettings_site.

Chaque test vérifie le comportement attendu d'une url
spécifique en utilisant le client de test Django.
Les urls testées incluent '/', '/404/', et '/500/'.
"""

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

# Instanciation du client de test
client = Client()


def test_index_url():
    """
    Test de l'URL pour la view 'index'
    """
    # Obtiens l'URL à partir du nom de la vue
    url = reverse('index')
    # Effectue une requête GET
    response = client.get(url)

    assert response.status_code == 200
    assert url == '/'
    assert resolve(url).view_name == "index"
    assertTemplateUsed(response, "index.html")


def test_404_url():
    """
    Test de l'url pour la view 'custom_404'
    """
    # Obtiens l'URL à partir du nom de la vue
    url = reverse('custom_404')
    # Effectuez une requête GET
    response = client.get(url)

    assert response.status_code == 404
    assert url == '/404/'
    assert resolve(url).view_name == "custom_404"
    assertTemplateUsed(response, "404.html")


def test_500_url():
    """
    Teste l'URL de la vue 'custom_500'.
    """
    # Obtiens l'URL à partir du nom de la vue
    url = reverse('custom_500')
    # Effectuez une requête GET
    response = client.get(url)

    assert response.status_code == 500
    assert url == '/500/'
    assert resolve(url).view_name == "custom_500"
    assertTemplateUsed(response, "500.html")


def test_admin_url():
    """
    Teste l'URL de la plateforme 'admin'.
    """
    # Obtiens l'URL à partir du nom de la vue
    url = reverse('admin:index')
    # Effectuez une requête GET
    response = client.get(url)

    # Redirection (status_code 302)
    assert response.status_code == 302
    assert url == '/admin/'
    assert resolve(url).view_name == "admin:index"

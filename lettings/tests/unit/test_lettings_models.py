"""
Module de tests unitaires pour les modèles de l'application 'lettings'.

Ce module contient des tests unitaires pour les modèles Address et
Letting de l'application 'lettings'.
Les tests vérifient la création d'instances, la représentation
sous forme de chaîne, et d'autres fonctionnalités
des modèles de l'application.
"""

import pytest
from django.test import Client
from lettings.models import Letting, Address


client = Client()


@pytest.mark.django_db
def test_address_model():
    """
    Test unitaire pour le modèle Address de l'application 'lettings'.

    Ce test crée une instance du modèle Address, vérifie que sa représentation
    sous forme de chaîne est correcte et correspond à la valeur attendue.
    """
    address = Address.objects.create(
        number=4,
        street="Privet Drive",
        city="Little Whinging",
        state="EA",
        zip_code=47839,
        country_iso_code="UK",
    )
    expected_value = "4 Privet Drive"
    assert str(address) == expected_value


@pytest.mark.django_db
def test_letting_model():
    """
    Test unitaire pour le modèle Letting de l'application 'lettings'.

    Ce test crée une instance du modèle Letting, vérifie que sa représentation
    sous forme de chaîne est correcte et correspond à la valeur attendue.
    """
    address = Address.objects.create(
        number=4,
        street="Privet Drive",
        city="Little Whinging",
        state="EA",
        zip_code=47839,
        country_iso_code="UK",
    )
    letting = Letting.objects.create(title="Harry Potter's House",
                                     address=address)
    expected_value = "Harry Potter's House"
    assert str(letting) == expected_value

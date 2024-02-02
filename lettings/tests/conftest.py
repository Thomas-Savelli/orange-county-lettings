"""
Module de configurations pour les tests de l'application 'lettings'.

Ce module contient des fixtures qui sont utilisées dans les tests
unitaires et d'intégration pour fournir des données
pré-configurées (comme les instances de modèles Address et Letting)
afin de simplifier la création
et l'exécution des tests.
"""

import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address_1():
    """
    Fixture pour créer une instance de modèle Address avec des valeurs spécifiques.

    Cette fixture crée et renvoie une instance
    du modèle Address avec des valeurs prédéfinies.
    Elle est utilisée dans les tests pour fournir une adresse spécifique.
    """
    address = Address.objects.create(
        number=4,
        street="Privet Drive",
        city="Little Whinging",
        state="EA",
        zip_code=47839,
        country_iso_code="UK",
    )
    return address


@pytest.fixture
def address_2():
    """
    Fixture pour créer une deuxième instance de modèle
    Address avec des valeurs spécifiques.

    Cette fixture crée et renvoie une deuxième instance
    du modèle Address avec des valeurs prédéfinies.
    Elle est utilisée dans les tests pour fournir
    une deuxième adresse spécifique.
    """
    address = Address.objects.create(
        number=12,
        street="Square Grimmaurd",
        city="Loutry Ste Chaspoule",
        state="DE",
        zip_code=89654,
        country_iso_code="UK",
    )
    return address


@pytest.fixture
def letting_1(address_1):
    """
    Fixture pour créer une instance de modèle Letting liée à address_1.

    Cette fixture crée et renvoie une instance du modèle
    Letting avec des valeurs prédéfinies
    et liée à l'adresse fournie en paramètre.
    Elle est utilisée dans les tests pour fournir
    un Letting spécifique lié à une adresse spécifique.
    """
    letting = Letting.objects.create(title="Harry Potter's House", address=address_1)
    return letting


@pytest.fixture
def letting_2(address_2):
    """
    Fixture pour créer une deuxième instance de
    modèle Letting liée à address_2.

    Cette fixture crée et renvoie une deuxième instance
    du modèle Letting avec des valeurs prédéfinies
    et liée à l'adresse fournie en paramètre. Elle est
    utilisée dans les tests pour fournir
    un deuxième Letting spécifique lié à
    une deuxième adresse spécifique.
    """
    letting = Letting.objects.create(title="The Burrow", address=address_2)
    return letting

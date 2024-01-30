"""
Module de définition des modèles pour l'application 'lettings'.

Ce module contient les définitions des modèles Django pour l'application 'lettings'.
Il inclut les modèles Address et Letting, qui représentent respectivement une adresse
et une location (letting) associée à une adresse.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse.

    Ce modèle représente une adresse avec des champs tels que le numéro, la rue, la ville, l'État,
    le code postal et le code ISO du pays. La méthode __str__ est définie pour fournir une représentation
    sous forme de chaîne de l'objet.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle représentant une location (letting).

    Ce modèle représente une location avec un titre et une adresse associée (relation OneToOne avec Address).
    La méthode __str__ est définie pour fournir une représentation sous forme de chaîne de l'objet.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

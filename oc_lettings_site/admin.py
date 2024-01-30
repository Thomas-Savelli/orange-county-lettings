"""
Ce module gère l'administration des modèles Letting, Address et Profile
via l'interface d'administration Django.
"""

from django.contrib import admin

from lettings.models import Letting
from lettings.models import Address
from profiles.models import Profile


# Enregistrement des modèles pour les gérer via l'interface d'administration Django
admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)

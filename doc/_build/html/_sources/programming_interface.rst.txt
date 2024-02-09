Interfaces de Programmation
===========================

Ce projet a entierement été codé avec django. De ce fait deux actions sont possibles :

Interface de programmation via le site d'administration de django
-----------------------------------------------------------------
Seulement accessible aux Super Utilisateurs, cette plateforme permet de gérer grace aux actions CRUD 
(Create, Read, Update et Delete) toutes les données de la Base de Données.

    Un Super Utilisateur a déja été crée dans la Base de Donnée mais si vous désirez en créer un nouveau,
    vous pouvez entrée cette commande dans votre terminal à la racine du projet :

    ``python manage.py createsuperuser``

    Vous n'avez plus qu'à repondre aux questions et votre super utilisateur sera créé.

Pour vous connecter à la plateforme administrative de Django, vous n'avez qu'à ajouter ``/admin/`` à la fin 
de votre URL. Que vous soyez en Local ou que vous utilisiez la version latest en ligne, la démarche est identique.
Renseigner les informations de votre super utilisateur est vous aurez accés à la plateforme.


Interface de Programmation via le Shell Python
----------------------------------------------

Moins intuitif que la plateforme d'administration de Django, celui-ci s'utilise simplement 
en entrant dans votre terminal à la racine du projet, la commande :

``python manage.py shell``

L'utilisation du Shell offre plusieurs avantages par rapport à l'interface 
administrative de Django (Django Admin) :

A - Exploration et Test Rapide :

Le shell interactif permet aux développeurs d'explorer rapidement la structure de leur application,
d'interroger la base de données, de tester des requêtes et d'expérimenter avec le code Python sans avoir
à passer par une interface utilisateur graphique.

B - Scripting et Automatisation :

Le shell est un excellent environnement pour écrire des scripts et automatiser des tâches.
Vous pouvez écrire des scripts pour manipuler les données, effectuer des opérations de maintenance
ou effectuer des tâches spécifiques à votre application.

C - Accès Direct à la Console Django ORM :

Le shell permet un accès direct à l'ORM (Object-Relational Mapping) de Django,
ce qui facilite l'exécution de requêtes sur la base de données sans avoir à créer des vues ou des modèles spécifiques.

D - Débogage Interactif :

En utilisant le shell interactif, vous pouvez déboguer votre application de manière interactive,
en inspectant les objets, en testant des fonctionnalités spécifiques et en comprenant le comportement
de votre code à un niveau plus profond.

E - Personnalisation et Contrôle :

Alors que l'interface administrative de Django offre une interface utilisateur prête à l'emploi pour la gestion des modèles,
le shell offre plus de flexibilité et de contrôle pour les développeurs qui souhaitent personnaliser ou automatiser des tâches spécifiques.

Pour plus d'information :

https://shell.readthedocs.io/en/latest/shell_api.html
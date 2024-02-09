Guide d'Utilisation
===================

Pour accéder à l'application web aprés le déploiement avec Render, vous pouvez utiliser l'URL suivante :

``https://oc-lettings-srth.onrender.com/``

Sur la page d'accueil, differents boutons vous permettrons de naviguer entre les differentes
pages de l'application pour pouvoir :

 - Consulter les profiles
 - Consulter le détail d'un profile en particulier
 - Consulter les locations
 - Consulter les détails d'une location en particulier


Voici une liste des differentes URLs de l'application : 

URLs principales :

    - ``/`` : Page d'accueil du site.
    - ``/lettings/`` : Liste des locations.
    - ``/lettings/<letting_id>/`` : Page détaillée d'une location.
    - ``/profiles/`` : Liste des profils utilisateurs.
    - ``/profiles/<username>/`` : Page détaillée d'un profil utilisateur.
    - ``/admin/`` : Interface de gestion administratif de Django.

URLs de gestions des erreurs :

    - ``/404/`` : Page personnalisée pour les erreurs 404.
    - ``/500/`` : Page personnalisée pour les erreurs 500.

URL pour effectuer un test de configuration de suivi des erreurs avecSentry :

    - ``/sentry-debug/`` : Page pour tester le suivi des erreurs avec Sentry.
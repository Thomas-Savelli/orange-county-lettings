Installation du projet
======================

Clone du repository
-------------------

Télécharger l’intégralité du repository sur : 

https://github.com/Thomas-Savelli/orange-county-lettings.git

Pour ce faire, veuillez ouvrir votre Terminal de Commande:

1. Grace à la commande cd , dirigez vous vers le répertoire ou vous voulez installer le repository exemple : ``cd Desktop`` 
*(pour l'installer sur le Desktop de votre ordinateur)*.

2. Par la suite, entrez dans votre terminal la commande : 

``git clone https://github.com/Thomas-Savelli/orange-county-lettings.git``

puis appuyer sur entrée afin de créer votre clone local.

Une fois le repository téléchargé et stocké localement, rendez vous dans le dossier du projet. Pour cela utiliser la commande :

``cd Python-OC-Lettings-FR``

Créer un environnement virtuel afin de récupérer les dépendances et packages du projet.

*(exemple procedure)* : ``python -m venv env``

Contrôler avec ``ls`` que vous disposez maintenant d’un dossier env. Si ce n’est pas le cas, réitérer cette étape en contrôlant la syntaxe de la ligne de commande. Sinon activer votre nouvel environnement virtuel.
  
    exemple procédure : 
    - (PowerShell): ``.\env\Scripts\activate`` 
    - (Windows): ``.\env\Scripts\activate.bat``
    - (autres): ``source env/bin/activate``

*Si vous rencontrez des difficultés vous pouvez vous référer sur le site :* 

https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789
  
  Pour contrôler la réussite de cette manœuvre, vous devriez avoir un ``(env)`` devant votre ligne de commande.

  PS : Taper seulement ``deactivate`` pour fermer ce dernier.

Pour finir, télécharger avec pip les packages et dépendances requis pour le bon fonctionnement du code avec le requirements.txt en entrant la commande suivante *(dans votre environnement virtuel !)* 

``pip install -r requirements.txt```

Une fois le téléchargement effectué et l'installation terminée, vous êtes prêt à exécuter le code.

Création du fichier ``.env``
------------------------------

Afin d'assurer une securité optimale, les données sensibles n'ont pas été intégrées au repository.
Veuillez donc à la racine du projet créer une fichier nommé : ``.env`` et veuillez y mettre les variables suivante :

``SECRET_KEY="la clé secrète du projet"``

``DSN="la clé dsn de sentry"``
 
La clé DSN de sentry, vous sera communiquée par Sentry https://sentry.io/signup/, lorsque vous aurez créer un compte et que vous aurez créer un projet. Vous n'aurez qu'à copier coller la valeur de la clé DSN.

Exécuter le site :
------------------
Dans le repertoire du projet en ayant votre ``env`` activé :
  - Tapez : ``python manage.py runserver``
  - Aller sur http://localhost:8000/ dans un navigateur.
  - Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
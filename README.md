<div style="display: flex; align-items: center; justify-content: center; margin-bottom: 30px;">
  <img src="./static/assets/img/logo.png" alt="Nom de l'image" width="150">
  <p style="font-family: 'Nom de la police'; font-size: 50px;margin-top: 40px;">ORANGE COUNTY LETTINGS</p>
</div>

![Version](https://img.shields.io/badge/Version-2.0-blue) ![Python](https://img.shields.io/badge/Python-3.11.1-green)

## Orange County Lettings - Application Web

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. Elle souhaite améliorer son site tant sur le code que sur le déploiement.

## Developpement

### Amélioration de la Version 2.0
  - Refonte de l'architecture modulaire dans le repository GitHub ;
  - Réduction de diverses dettes techniques sur le projet ;
  - Ajout d'un pipeline CI/CD ainsi que son déploiement ;
  - Surveillance de l’application et suivi des erreurs via Sentry ;
  - Création de la documentation technique de l'application avec Read The Docs et Sphinx.

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### Installation
Télécharger l’intégralité du repository sur : https://github.com/Thomas-Savelli/orange-county-lettings.git

Pour ce faire, veuillez ouvrir votre Terminal de Commande: 

1. Grace à la commande cd , dirigez vous vers le répertoire ou vous voulez installer le repository exemple : ```cd Desktop``` *(pour l'installer sur le Desktop de votre ordinateur)*.

2. Par la suite, entrez dans votre terminal la commande : 
```
git clone https://github.com/Thomas-Savelli/orange-county-lettings.git
```
puis appuyer sur entrée afin de créer votre clone local.

Une fois le repository téléchargé et stocké localement, rendez vous dans le dossier du projet. Pour cela utiliser la commande : ```cd Python-OC-Lettings-FR```

- Créer un environnement virtuel afin de récupérer les dépendances et packages du projet.  
*exemple procedure* : ```python -m venv env```
- Contrôler avec ```ls``` que vous disposez maintenant d’un dossier env. Si ce n’est pas le cas, réitérer cette étape en contrôlant la syntaxe de la ligne de commande. Sinon activer votre nouvel environnement virtuel.
  
    exemple procédure : 
    - (PowerShell): ```.\env\Scripts\activate``` 
    - (Windows): ```.\env\Scripts\activate.bat```
    - (autres): ```source env/bin/activate```

*Si vous rencontrez des difficultés vous pouvez vous référer sur le site :* https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789
  
  Pour contrôler la réussite de cette manœuvre, vous devriez avoir un ```(env)``` devant votre ligne de commande.

  PS : Taper seulement ```deactivate``` pour fermer ce dernier.

Pour finir, télécharger avec pip les packages et dépendances requis pour le bon fonctionnement du code avec le requirements.txt en entrant la commande suivante *(dans votre environnement virtuel !)* 

```pip install -r requirements.txt``` 

Une fois le téléchargement effectué et l'installation terminée, vous êtes prêt à exécuter le code.

### Création du fichier ```.env```
Afin d'assurer une securité optimale, les données sensibles n'ont pas été intégrées au repository.
Veuillez donc à la racine du projet créer une fichier nommé : ```.env``` et veuillez y mettre les variables suivante :
```SECRET_KEY="la clé secrète du projet"```
```DSN="la clé dsn de sentry"```

> NOTES : 
> La clé DSN de sentry, vous sera communiquée par Sentry (*https://sentry.io/signup/*), lorsque vous aurez créer un compte et que vous aurez créer un projet. Vous n'aurez qu'à copier coller la valeur de la clé DSN.

### Exécuter le site
Dans le repertoire du projet en ayant votre ```env``` activé :
  - Tapez : `python manage.py runserver`
  - Aller sur `http://localhost:8000` dans un navigateur.
  - Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

### Exécuter le Linting
Afin de tester manuellement le linting du projet, positionnez-vous dans le repertoire racine du projet et (```env``` activé) tapez :
- `flake8 .`

### Exécuter les Tests
Afin de tester manuellement les tests du projet, positionnez-vous dans le repertoire racine du projet et (```env``` activé) tapez :

- `pytest`

Si vous désirez effectuer les tests du projet avec une couverture de tests, vous pouvez utiliser cette commande :

- ```pytest --cov=.```

Et si vous désirez également générer un nouveau rapport html de couverture de tests, vous pouvez utiliser cette commande : 
- ```pytest --cov=. --cov-report html```

### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Deploiement
Le déploiement a été automatisé de façon à ce que chaque commit sur la branche ```main``` du repository entraine l'éxecution au préalable de plusieurs étapes. Celles ci sont gérer à l'aide de la Pipeline CI-CD (```.github/workflows/ci-cd.yml```).

Voici la liste chronologique des étapes de la Pipeline :
- Reproduction de l'environement de développement local
- Vérification du formatage du code (Linting)
- Déclenchement des tests du projet
- Vérification que la couverture de tests soit supérieur à 80%

Si une étape n'est pas valide et renvoie une erreur, cela n'exécutera pas la suite de la Pipeline. Si toutes ces étapes sont validées alors la Pipeline éxécutera sa derniere action qui est la Conteneurisation du projet avec Docker :
- Création de deux images Docker :
  - une image Docker avec le tag : ```latest``` (Derniére version stable)
  - une image Docker avec le tag du dernier commit. (Permet de mieux gérer le systéme de version)
- Push des images Docker sur DockerHub

Une fois que la Pipeline a été exécuter correctement sans retour d'erreur, nos images sont donc disponible sur DockerHub et notre hébergeur Render récupére automatique notre image Docker: ```latest``` , ce qui permet de garder notre projet à jour.

> Note : 
> le fichier ```ci-cd-other.yml``` concerne les commits des autres branches et par conséquent ne prend pas en charge les modifications de la branche principal ```main``` ! 
> Ce fichier se comporte de la même maniére que ```ci-cd.yml``` si ce n'est que la Pipeline n'effectue que les 4 premiéres étapes ( de la reproduction de l'environement à la vérification de la couverture de tests ) .

### Prérequis
- Votre compte GitHub
- Compte Sentry (*https://sentry.io/signup/*)
- Compte Docker Hub (*https://hub.docker.com/*)
- Compte Render (*https://render.com/*)

### Etape de configuration 

> Note : 
> Veuillez à avoir bien suivi l'étape de développement : ```Création d'un fichier .env```

#### 1 - Utilisation de GitHub Actions

Une foie que vous vous êtes créer un compte sur DockerHub :

  - Rendez-vous dans le repository GitHub du projet que vous aurez au préalablement pusher sur votre compte distant.

  - Puis cliquez sur ```Settings``` dans la barre horizontale au dessus de vos fichiers.

  - Dans la barre latérale gauche, selectionner ```Secrets and variables``` puis cliquez sur ```Actions```.

  - Vous pouvez ensuite en base de la page (section Secrets), créez de nouveaux repository secrets. Veuillez creer les variables secretes suivantes : 
    - DSN (Votre key DSN de Sentry)
    - SECRET_KEY (Votre secrete key de django)
    - DOCKERHUB_USERNAME (Votre Username de connexion DockerHub)
    - DOCKER_PASSWORD (Votre mot de passe pour une connexion DockerHub)
  
  - Ceci étant fais, créer un nouveau commit et pusher le projet sur votre repository.

  - Rendez-vous dans votre repository et cliquer sur Actions dans la barre horizontale au dessus du projet. Normalement vous devez constater deux plusieurs choses :
    - La premiére est que dans la barre latérale droite, vous disposez des deux Pipelines ( ```ci-cd.yml``` & ```ci-cd-other.yml``` ).
    - En cliquant sur ```ci-cd.yml``` vous devez normalement avoir deux workflows. 
      - Un workflow (le premier) qui est vert donc qui a reussi.Il correspond au dernier commit que vous venez d'effectuer.
      - Un workflow (le dernier) qui est rouge et donc qui a échoué. Il correspond au premier push que vous avez effectuer avant de renseigner vos variables secrets dans GitHub.
  
#### 2 - Configuration de l'hébergeur Render

Rendez vous sur le site de l'hébergeur Render et créez vous un compte. Différentes options s'offrent à vous, sachez que n'utilisant pas l'option ssh, la version gratuite est amplement suffisante pour que le deploiement soit réussi. Toutefois, si vous choisiez la version gratuite, sachez que les services peuvent nécéssiter plus de temps pour fonctionner.

Une fois que votre compte est créer :
  - Cliquez sur ```New``` puis ```Web Service``` pour créer une nouvelle instance.
  - Choisissez la méthode : ```Deploy an existing image from a registry```
  - Dans Image Url, veuillez renseigner l'url de votre image Docker. 
  - Ceci fait, vous vous retrouvez devant les logs de votre application. Une fois que le message "Your service is live" apparait dans vos logs, votre application est en ligne ! 



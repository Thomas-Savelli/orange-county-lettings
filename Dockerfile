# Utilisation d'une image de base
FROM python:3.11.1

# Définission du répertoire de travail
WORKDIR /usr/src/app

# Configure l'environnement Python pour éviter la création de fichiers .pyc (bytecode) lors de l'exécution de scripts.
ENV PYTHONDONTWRITEBYTECODE 1

# Désactive la mise en mémoire tampon de la sortie standard et d'erreur, ce qui est recommandé pour les applications Docker.
ENV PYTHONUNBUFFERED 1

# Copie les fichiers du projet dans le répertoire de travail du conteneur
COPY . /usr/src/app/

# Met à jour l'outil pip à la dernière version disponible.
RUN pip install --upgrade pip

# Installation des dépendences à partir de requirements.txt
RUN pip install -r requirements.txt

# Collecte les fichiers statiques de l'application Django dans un répertoire spécifié. Utile lors du déploiement
RUN python manage.py collectstatic --noinput

# Informe Docker que l'application écoute sur le port 8000
EXPOSE 8000

# Définit la commande par défaut qui sera exécutée lorsque le conteneur sera démarré (Lancement du serveur Django)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
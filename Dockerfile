# Utiliser une image de base officielle avec Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances si un fichier requirements.txt est présent
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5050

# Commande par défaut (à modifier selon votre projet)
CMD ["python", "app.py"]

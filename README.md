# Web Scraper Python - Veille Concurrentielle & Démo
## Origine du projet
Ce projet est né d'une mission confiée par mon tuteur durant un stage, dont l'objectif était d'automatiser la récupération des tarifs et des services proposés par des sites concurrents dans le cadre d'une veilleconcurrentielle.
Cette version ci est adaptater pour faire une démonstration : le script scrape mon propre portfolio au lieu de sites concurrents afin d'illustrer la logique d'extraction et d'export de données.

## Technologies utilisées
Python 3
requests – récupération du contenu HTML
BeautifulSoup (bs4) – parsing et navigation dans le HTML
csv / datetime – modules natifs Python pour l'export et l'horodatage

## Installation
### Installer les bibliothèques Python nécessaire
Ouvrez votre terminal et exécutez la commande suivante pour installer les dépendances nécessaires :
pip install requests beautifulsoup4
### Lancer le script
Web_Scraper.py
### Résultat
Un fichier portfolio_data.csv est généré avec toutes les données extraites et la date d'extraction.

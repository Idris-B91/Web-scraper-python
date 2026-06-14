import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# CONFIGURATION
url = "https://idris-b91.github.io/Mon-CV/"
nom_fichier_csv = "portfolio_data.csv"
date_scraping = datetime.now().strftime("%d/%m/%Y %H:%M")

# ÉTAPE 1 : REQUÊTE
print("Connexion au site...")
response = requests.get(url)

if response.status_code == 200:
    print("Connexion réussie !")
else:
    print(f"Erreur : {response.status_code}")
    exit()

# ÉTAPE 2 : PARSER LE HTML
soup = BeautifulSoup(response.text, "html.parser")

# ÉTAPE 3 : EXTRAIRE CHAQUE SECTION DE MON PORTFOLIO
# SECTION PRÉSENTATION
section_presentation = soup.find("section", id="presentation")
paragraphe = section_presentation.find("p")
texte_presentation = paragraphe.text.strip()

# SECTION FORMATION
section_formation = soup.find("section", id="formation")
articles_formation = section_formation.find_all("article")
texte_formation = ""

for article in articles_formation:
    
    h3 = article.find("h3") 
    p = article.find("p")
    texte_formation += h3.text.strip() + " — " + p.text.strip() + "\n"

# SECTION EXPÉRIENCE
section_experience = soup.find("section", id="experience")
articles_experience = section_experience.find_all("article")

texte_experience = ""

for article in articles_experience:

    h3 = article.find("h3")
    p = article.find("p")
    texte_experience += h3.text.strip() + "\n"
    texte_experience += p.text.strip() + "\n"
    taches = article.find_all("li")

    for tache in taches:
        texte_experience += "• " + tache.text.strip() + "\n"
    texte_experience += "\n"

# SECTION COMPÉTENCES
section_competences = soup.find("section", id="competences")
texte_competences = section_competences.get_text(separator="\n", strip=True)

# SECTION CENTRES D'INTÉRÊT
section_interets = soup.find("section", id="centres-interet")
items_interets = section_interets.find_all("li")
texte_interets = ""
for item in items_interets:
    texte_interets += "• " + item.text.strip() + "\n"

# ÉTAPE 4 : EXPORT DES DONNÉES VERS CSV
print(f"\nExport vers {nom_fichier_csv}...")

with open(nom_fichier_csv, "w", newline="", encoding="utf-8") as fichier:
    
    colonnes = ["date", "section", "contenu"]
    writer = csv.DictWriter(fichier, fieldnames=colonnes)
    
    writer.writeheader()
    
    # Ecrit une ligne par section
    writer.writerow({"date": date_scraping, "section": "Présentation",             "contenu": texte_presentation})
    writer.writerow({"date": date_scraping, "section": "Formation",                "contenu": texte_formation})
    writer.writerow({"date": date_scraping, "section": "Expérience",               "contenu": texte_experience})
    writer.writerow({"date": date_scraping, "section": "Compétences",              "contenu": texte_competences})
    writer.writerow({"date": date_scraping, "section": "Centres d'intérêt",        "contenu": texte_interets})

print("Export terminé !")
print(f"Ouvre {nom_fichier_csv} dans Excel pour voir le résultat.")
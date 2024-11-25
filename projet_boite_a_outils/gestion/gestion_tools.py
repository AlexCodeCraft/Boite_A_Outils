import csv
from outils.tournevis import Tournevis
from outils.marteau import Marteau
from outils.cle_plate import ClePlate
from outils.perceuse import Perceuse
from outils.foret import Foret

def charger_outils(fichier):
    outils = []
    with open(fichier, newline='', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip header
        for row in reader:
            type, sous_type, taille, etat, emprunt, date_emprunt, usage = row
            # Ajouter l'outil correspondant à son type
            if type == "Tournevis":
                outils.append(Tournevis(sous_type, taille, etat, emprunt, date_emprunt, int(usage)))
            elif type == "Marteau":
                outils.append(Marteau(sous_type, taille, etat, emprunt, date_emprunt, int(usage)))
            elif type == "Clé Plate":
                outils.append(ClePlate(taille, etat, emprunt, date_emprunt, int(usage)))
            elif type == "Perceuse":
                outils.append(Perceuse(taille, etat, emprunt, date_emprunt, int(usage)))
            elif type == "Forêt":
                outils.append(Foret(sous_type, taille, etat, emprunt, date_emprunt, int(usage)))
    return outils

def sauvegarder_outils(outils, fichier):
    with open(fichier, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Type', 'sous-type', 'taille', 'Etat', 'Emprunt', 'date emprunt', 'usage'])
        for outil in outils:
            writer.writerow([outil.type, outil.sous_type, outil.taille, outil.etat, outil.emprunt, outil.date_emprunt, outil.usage])

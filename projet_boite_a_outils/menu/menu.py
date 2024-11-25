from gestion.gestion_tools import charger_outils, sauvegarder_outils
from outils.tournevis import Tournevis
from outils.marteau import Marteau
from outils.cle_plate import ClePlate
from outils.perceuse import Perceuse
from outils.foret import Foret

def afficher_menu(outils):
    while True:
        print("\nMenu:")
        print("1. Liste des outils")
        print("2. Emprunter un outil")
        print("3. Restituer un outil")
        print("4. Utiliser un outil")
        print("5. Sauvegarder l'état")
        print("6. Quitter")
        choix = input("Choisissez une option: ")

        if choix == '1':
            lister_outils(outils)
        elif choix == '2':
            emprunter_outil(outils)
        elif choix == '3':
            restituer_outil(outils)
        elif choix == '4':
            utiliser_outil(outils)
        elif choix == '5':
            sauvegarder_outils(outils, 'data/toolbox.csv')
        elif choix == '6':
            break

def lister_outils(outils):
    for outil in outils:
        print(f"{outil.type} {outil.sous_type} ({outil.taille}) - Etat: {outil.etat}")

def emprunter_outil(outils):
    print("Quel outil voulez-vous emprunter ?")
    for i, outil in enumerate(outils, start=1):
        print(f"{i}. {outil.type} {outil.sous_type} ({outil.taille}) - Etat: {outil.etat}")
    
    choix = int(input("Entrez le numéro de l'outil: "))
    outil_choisi = outils[choix - 1]

    if outil_choisi.etat == 'Dispo':
        nom_ouvrier = input("Entrez le nom de l'ouvrier qui emprunte l'outil: ")
        date_emprunt = input("Entrez la date d'emprunt (ex: JJ/MM/AAAA): ")
        outil_choisi.emprunter(nom_ouvrier, date_emprunt)
        print(f"L'outil {outil_choisi.type} {outil_choisi.sous_type} a été emprunté par {nom_ouvrier}.")
    else:
        print(f"L'outil {outil_choisi.type} {outil_choisi.sous_type} n'est pas disponible.")

def restituer_outil(outils):
    print("Quel outil voulez-vous restituer ?")
    for i, outil in enumerate(outils, start=1):
        print(f"{i}. {outil.type} {outil.sous_type} ({outil.taille}) - Etat: {outil.etat}")
    
    choix = int(input("Entrez le numéro de l'outil: "))
    outil_choisi = outils[choix - 1]

    if outil_choisi.etat == 'Emprunté':
        outil_choisi.restituer()
        print(f"L'outil {outil_choisi.type} {outil_choisi.sous_type} a été restitué.")
    else:
        print(f"L'outil {outil_choisi.type} {outil_choisi.sous_type} n'est pas emprunté.")

def utiliser_outil(outils):
    print("Quel outil voulez-vous utiliser ?")
    for i, outil in enumerate(outils, start=1):
        print(f"{i}. {outil.type} {outil.sous_type} ({outil.taille}) - Etat: {outil.etat}")
    
    choix = int(input("Entrez le numéro de l'outil: "))
    outil_choisi = outils[choix - 1]

    if isinstance(outil_choisi, Tournevis):
        action = input("Voulez-vous visser ou dévisser ? (vissser/dévisser): ")
        if action == 'visser':
            outil_choisi.visser()
        elif action == 'dévisser':
            outil_choisi.devisser()
        print(f"Le tournevis a été utilisé pour {action}.")
    elif isinstance(outil_choisi, Marteau):
        outil_choisi.planter_clou()
        print("Le marteau a été utilisé pour planter un clou.")
    elif isinstance(outil_choisi, ClePlate):
        outil_choisi.utiliser()
        print("La clé plate a été utilisée.")
    elif isinstance(outil_choisi, Perceuse):
        outil_choisi.percer()
        print("La perceuse a été utilisée.")
    elif isinstance(outil_choisi, Foret):
        outil_choisi.percer()
        print("Le foret a été utilisé.")

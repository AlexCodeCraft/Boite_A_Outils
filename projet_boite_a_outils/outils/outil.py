class Outil:
    def __init__(self, type, sous_type, taille, etat="Dispo", emprunt="no", date_emprunt="", usage=0):
        self.type = type
        self.sous_type = sous_type
        self.taille = taille
        self.etat = etat
        self.emprunt = emprunt
        self.date_emprunt = date_emprunt
        self.usage = usage

    def emprunter(self, nom_ouvrier, date_emprunt):
        self.etat = "Emprunté"
        self.emprunt = nom_ouvrier
        self.date_emprunt = date_emprunt

    def restituer(self):
        self.etat = "Dispo"
        self.emprunt = "no"
        self.date_emprunt = ""
    
    def increment_usage(self):
        self.usage += 1

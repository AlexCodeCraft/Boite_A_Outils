from .outil import Outil

class Foret(Outil):
    def __init__(self, sous_type, taille, etat="Dispo", emprunt="no", date_emprunt="", usage=0):
        super().__init__("Forêt", sous_type, taille, etat, emprunt, date_emprunt, usage)
    
    def percer(self):
        self.increment_usage()
        print("Percer un trou avec le foret !")

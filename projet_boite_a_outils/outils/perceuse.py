from .outil import Outil

class Perceuse(Outil):
    def __init__(self, taille, etat="Dispo", emprunt="no", date_emprunt="", usage=0):
        super().__init__("Perceuse", "", taille, etat, emprunt, date_emprunt, usage)
    
    def percer(self):
        self.increment_usage()
        print("Percer un trou !")

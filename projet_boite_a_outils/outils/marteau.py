from .outil import Outil

class Marteau(Outil):
    def __init__(self, sous_type, taille, etat="Dispo", emprunt="no", date_emprunt="", usage=0):
        super().__init__("Marteau", sous_type, taille, etat, emprunt, date_emprunt, usage)
    
    def planter_clou(self):
        self.increment_usage()
        print("Planter un clou !")

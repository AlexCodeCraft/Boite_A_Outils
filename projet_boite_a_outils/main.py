from menu.menu import afficher_menu
from gestion.gestion_tools import charger_outils

if __name__ == "__main__":
    outils = charger_outils("data/toolbox.csv")
    afficher_menu(outils)

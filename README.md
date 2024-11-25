# Projet : Boîte à Outils

## Description
Ce projet implémente une gestion d'une boîte à outils en Python. 
Chaque outil a ses propres fonctionnalités, et les emprunts d'outils par des utilisateurs sont gérés via un menu interactif.

### Fonctionnalités principales :
- Gestion des outils : tournevis, marteaux, clés plates, perceuses, forêts.
- Système de prêt et restitution des outils avec suivi de disponibilité.
- Utilisation des outils avec incrémentation des usages.
- Export de l'état de la boîte à outils vers un fichier CSV.

---

## Architecture du Projet
📂 PROJET_BOITE_A_OUTILS
│
├── 📂 data
│ └── toolbox.csv - Le fichier source contenant les outils disponibles.
│
├── 📂 gestion
│ └── gestion_tools.py - Gestion des emprunts et restitutions.
│
├── 📂 menu
│ └── menu.py - Menu interactif pour l'utilisateur.
│
├── 📂 outils
│ ├── outil.py - Classe principale Outil.
│ ├── tournevis.py - Classe pour les tournevis.
│ ├── marteau.py - Classe pour les marteaux.
│ ├── cle_plate.py - Classe pour les clés plates.
│ ├── perceuse.py - Classe pour les perceuses.
│ └── foret.py - Classe pour les forêts.
│
└── main.py - Point d'entrée du programme.

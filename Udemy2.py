
"""

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
del employes["id03"]
employes["id02"]["age"] = employes["id02"]["age"] + 1 
print(employes["id02"]["age"])
Paul_Age = employes["id01"]["age"]
print(Paul_Age)

"""

"""
from pathlib import *

Tri = {".mp3" : "Musique",
       ".wav" : "Musique",
       ".flac" : "Musique",
       ".avi" : "Videos",
       ".mp4" : "Videos",
       ".gif" : "Videos",
       ".bmp" : "Images",
       ".jpg" : "Images",
       ".png" : "Images",
       ".txt" : "Documents",
       ".pptx" : "Documents",
       ".csv" : "Documents",
       ".xls" : "Documents",
       ".odp" : "Documents",
       ".pages" : "Documents"
       } 
Dossier = Path.home() / "Downloads"
contenu_Total = Dossier.iterdir()
contenu_fichier = [ f for f in contenu_Total if f.is_file() ] 
for f in contenu_fichier :
    if f.suffix in Tri :
        Sortie = Dossier / Tri.get(f.suffix, "Autres")
        Sortie.mkdir(exist_ok = True)
        f.rename(Sortie / f.name)
    else :
        Sortie = Dossier / "Autres"
        Sortie.mkdir(exist_ok = True)
        f.rename(Sortie / f.name)

"""

"""
from pathlib import *

chemin = Path.home() / "Documents"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

p = list(d.keys())
for f in p :
    p = chemin / f 
    p.mkdir(exist_ok = True)
    w = d[f]
    for i in w :
        n = p / i
        n.mkdir(exist_ok = True)

"""
"""
from pathlib import *

chemin = Path.home() / "prenom.txt"
with open(chemin, "r") as f :
    lines = f.read().splitlines()

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]

with open(chemin, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))

"""
"""
from pathlib import *

fichier = input("Entrer le fichier dans lequel vous voulez entrer : ")
chemin = Path.home() / "Downloads" / fichier 

try :
    with open(chemin, "r") as f :
        a = 1 + 2
except TypeError as e :
    print(f"Erreur : {e}") 
except UnicodeDecodeError as e :
    print(f"Erreur : {e}")
except FileNotFoundError as e :
    print(f"Erreur : {e}")
else :
    print("OK mon pote")
    
"""


def multiplicateur_mot(mult=5, mot="Bonsoir"):
	return mot * mult

mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)

# Manipulation int et str

"""
a = "J'ai une classe de " + str(30) + " élèves"
b = "10" + " + " + "5" + " est égal à " + "15"
c = 10 + int("5")
d = "L'addition de 10 + 5 est égal à " + str(10 + 5)

print(a)
print(b)
print(c)
print(d)

"""
#Exo input
"""

prenom = input("Quel est votre prenom ?")
ville_de_naissance = input("Quelle est votre ville de naissance ?")
age = input("Quel est votre age ?")
print(prenom)
print(ville_de_naissance)
print(age)

"""
#Split/Join/Sort ou sorted
"""

chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_2 = chaine.split(" ,")
chaine_3 = sorted(chaine_2)
chaine_en_ordre = " ,".join(chaine_3)
print(chaine_en_ordre)

"""
#Calculatrice1
"""
print("Bonjour vous allez utiliser une calculattrice uniquement pour les additions")
a = int(input("Veuillez rentrer votre premier chiffre ou nombre à additionner"))
b = int(input("Veuillez rentrer le second chiffre à additionner "))
print(f"Le reslutat de l'addition de {a} et de {b} est égal à {a + b}")

"""
#Manipulation liste avec debut fin et le pas

"""

liste = [1, 2, 3, 4, 5]
print(liste[::len(liste)-1])

"""
#Exo mdp
"""

mdp = input("Entrez un mot de passe (min 8 caractères) : ")

mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0:
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())



for i in range(10):
    print(f"Utilisateur {i+1}")

"""
#Mettre un mot rentré à l'envers
"""

mot = input("rentrez un mot")
mot_a_l_envers = reversed(mot)
for i in mot_a_l_envers:
    print(i)


nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]

print(nombres_pairs)
"""
#Manipulation liste2
"""
# ---------------------------------------------------- #

nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]

print(nombres_positifs)

# ---------------------------------------------------- #

nombres = range(5)
nombres_doubles = [i*2 for i in nombres]

print(nombres_doubles)

# ---------------------------------------------------- #

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]

print(nombres_inverses)

"""
#ma technique à moi pour la calculatrice#

"""
a = input("Veuillez rentrer le premier nombre à multiplier")
x = a.isdigit()

while x  == False:
    print("La valeur rentré n'est pas un nombre")
    a = input("Veuillez rentrer le premier nombre à multiplier")
    x = a.isdigit()

a = int(a)
b = input("Veuillez rentrer le second nombre à multiplier")
y = b.isdigit()

while y  == False:
    print("La valeur rentré n'est pas un nombre")
    b = input("Veuillez rentrer le second nombre à multiplier")
    y = b.isdigit()

b = int(b)
print(f"Le résultat de l'addition de {a} avec {b} est égal à {a+b}")
"""

#Technique du prof#
"""
a = b = ""

# Tant que a et b ne sont pas des nombres, on boucle
while not (a.isdigit() and b.isdigit()):
    
    # On demande deux nombres à l'utilisateur
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    
    # On affiche une phrase si les nombres entrés ne sont pas valides.
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

# On affiche le résultat de l'addition
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")

"""
#Exercice Liste#

"""
nombre = 0
Liste_de_courses = []
while nombre != 5:
    print("1. Ajouter un élement à la liste.")
    print("2. Retirer un élement de la liste.")
    print("3. Afficher les élements à la liste.")
    print("4. Vider la liste.")
    print("5. Quitter")
    nombre = int(input("Quel est votre choix ?:"))
    if nombre == 1:
        Liste_de_courses.append(input("Que voulez-vous ajouter ?:"))
        print(f"L'element {Liste_de_courses[-1]} à bien été ajouté à la liste")
        pass
    elif nombre == 2:
        element = input("Que voulez vous sortir de votre liste ?:")
        if element in Liste_de_courses:
            Liste_de_courses.remove(element)
            print(f"L'element {element} à bien été retiré de la liste")
        else:
            print(f"L'element {element} n'est pas dans la liste") 
        pass
    elif nombre == 3:
        if Liste_de_courses: #Vérifie la condition que la liste contient des elements
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(Liste_de_courses, 1):  # Le 1 de enumerate veut dire qu'on veut commencer par le 1
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
        pass
    elif nombre == 4:
        Liste_de_courses.clear
        print("La liste à été vidé")
        pass
    elif nombre == 5:
        print("A bientot")
        break
    else:
        print("La valeur que vous avez rentré n'est pas valide")
        pass
    print ("-" * 50)

"""
#Exercice devinette ma version

"""

import random

print("Bonjour Vous venez d'entrer dans le jeu des devinettes.")
Maximum = "a"
Digit = Maximum.isdigit()

while Digit == False:
    Maximum = input("Entrez un nombre pour signifier le maximum possible.")
    Digit = Maximum.isdigit()
    if Digit == False:
        print("La valeur que vous avez rentré n'est pas accéptée, veuillez re-essayer.")
    else:
        Maximum = int(Maximum)
        pass

chance = 5
Aleatoire = random.randint(0, Maximum)
essai = -1

while chance > 0 or essai != Aleatoire:
    essai = input("Quel est votre nombre ?")
    Digit = essai.isdigit()
    print("_" * 50)
    if Digit == False:
        print("La valeur que vous avez rentré n'est pas valable.")
        print("_" * 50)
        pass
    else:
        essai = int(essai)
        if essai > Aleatoire :
            print(f"{essai} est supérieur à la valeur attendue, veuillez re-essayer.")
            chance -= 1
            print(f"Il vous reste {chance} essais")
            print("_" * 50)
        elif essai < Aleatoire :
            print(f"{essai} est inférieur à la valeur attendue, veuillez re-essayer.")
            chance -= 1
            print(f"Il vous reste {chance} essais")
            print("_" * 50)
        else :
            print(f"Bravo !! {essai} était la bonne valeur attendue ! avec seulement {5-chance} essais")

if chance == 0:
    print("Vous avez lamentablement perdu")    

SystemExit

"""
#Jeu de rôle
"""
"""
"""
import random

VieHeros = 50
VieEnnemie = 50
PotionHeros = 3
Choix = "a"

print("_" * 50)
print("Vous venez de tomber contre un ennemie, vous devez vous battre !!!")
print("_ " * 50)

while VieHeros >= 0 and VieEnnemie >= 0:
    print(f"Votre vie est de {VieHeros}❤️  et celle de votre ennemie est à {VieEnnemie}❤️.")
    print("")
    Choix = input("Vous avez le choix entre:\n -Attaquer:(1)⚔️\n -Prendre une potion:(2)❤️\n Que choisissez vous ?")
    Digit = Choix.isdigit()
    print("")
    if Digit == False :
        print("La valeur que vous venez de rentrer n'est pas valide veuillez recommencer.")
        print("_ " * 50)
    else :
        Choix = int(Choix)
        if Choix == 1:
            AttaqueHeros = random.randint(5, 10)
            AttaqueEnnemie = random.randint(5, 15)
            print(f"Vous avez infligés {AttaqueHeros} de dégats ⚔️  à votre ennemie")
            print(f"Mais votre ennemie vous inflige {AttaqueEnnemie} de dégats ⚔️")
            print("")
            VieHeros = (VieHeros - AttaqueEnnemie)
            VieEnnemie = (VieEnnemie - AttaqueHeros)
            print("_ " * 50)
            print("")
        elif Choix == 2 :
            if PotionHeros > 0:
                PotionHeros -= 1
                Potion = random.randint(15, 50)
                AttaqueEnnemie = random.randint(5, 15)
                print(f"Votre potion vous permet de récuperer {Potion} de points de vie ❤️.  Il vous reste {PotionHeros} potions")
                print(f"Mais votre ennemie vous inflige {AttaqueEnnemie} de dégats ⚔️")
                print("")
                VieHeros = (VieHeros + Potion)
                VieHeros = (VieHeros - AttaqueEnnemie)
                print("_ " * 50)
                print("")
            else :
                print("Vous n'avez plus de potions !")
        else :
            print("La nombre rentré ne correspond à aucune des possibilités veuillez re-essayer")
            print("_ " * 50)
            print("")

if VieHeros <= 0:
    print("Votre vie est tombée à 0.\nVous avez perdu ! Votre ennemie vous viole, dépouille de vos biens et jette votre cadavre fumant à manger aux cochons")
    SystemExit
else :
    print("La vie de votre adversaire tombe à 0.\nVous avez gagné ! Vous accrochez donc la tête de votre ennemie à un pique et partez en héros demander la main de la princesse au roi")
    SystemExit

"""

"""
#Chemin vers mes documents
MesDocuments = r"C:\ Users\ nathan.dubroc"

MesDocuments_txt = MesDocuments + r"\Python.txt"
print(MesDocuments_txt)

#Ouvrir un fichier avec python

f = open(MesDocuments_txt, "r")     #Sert à ouvrir le fichier
f.close()                       #Sert à le fermer, ne pas oublier

#Ou alors
with open(MesDocuments_txt, "r") as f:  #Ouvre le fichier dans la boucle with
    pass                            #Sert à le fermer

with open(MesDocuments_txt, "a") as f :
    f.write("Ceci est mon premier texte en \nPyhton")


import json 

with open("data.json", "r") as f:
    contenu = json.load(f)

contenu.append(64)

with open("data.json", "w") as f:
    json.dump(contenu, f)

"""
"""
import json

nombre = 0
Liste_de_courses = []
while nombre != 5:
    print("1. Ajouter un élement à la liste.")
    print("2. Retirer un élement de la liste.")
    print("3. Afficher les élements à la liste.")
    print("4. Vider la liste.")
    print("5. Quitter")
    nombre = input("Quel est votre choix ?:")
    digit = nombre.isdigit()
    while digit == False :
        print ("_ " * 50)
        print(" ")
        print("La valeur que vous avez rentré n'est pas un nombre")
        nombre = input("Quel est votre choix ?:")
        digit = nombre.isdigit()
    nombre = int(nombre)
    if nombre == 1:
        with open("data.json", "r") as f :
            Liste_de_courses = json.load(f)
            print ("_ " * 50)
            print(" ")
            ajout = input("Que voulez-vous ajouter ?:")
            if ajout in Liste_de_courses :
                print("L'element que vous essayez d'ajouter est déjà dans votre liste de courses")
            else :
                Liste_de_courses.append(ajout)           
        with open("data.json", "w") as f :
            json.dump(Liste_de_courses, f)
            print(f"L'element {Liste_de_courses[-1]} à bien été ajouté à la liste")
        pass
    elif nombre == 2:
        print ("_ " * 50)
        print(" ")
        element = input("Que voulez vous sortir de votre liste ?:")
        if element in Liste_de_courses:
            with open("data.json", "r") as f :
                Liste_de_courses = json.load(f)
                Liste_de_courses.remove(element)
            with open("data.json", "w") as f :
                json.dump(Liste_de_courses, f)
            print(f"L'element {element} à bien été retiré de la liste")
        else:
            print(f"L'element {element} n'est pas dans la liste") 
        pass
    elif nombre == 3:
        print ("_ " * 50)
        print(" ")
        with open("data.json", "r") as f :
            Liste_de_courses = json.load(f)
        if Liste_de_courses: #Vérifie la condition que la liste contient des elements
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(Liste_de_courses, 1):  # Le 1 de enumerate veut dire qu'on veut commencer par le 1
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
        pass
    elif nombre == 4:
        print ("_ " * 50)
        print(" ")
        with open("data.json", "r") as f :
            Liste_de_courses = json.load(f)
            Liste_de_courses.clear
        with open("data.json", "w") as f :
            json.dump(Liste_de_courses, f)
        print("La liste à été vidé")
        pass
    elif nombre == 5:
        print ("_ " * 50)
        print(" ")
        print("A bientot")
        break
    else:
        print ("_ " * 50)
        print(" ")
        print("La valeur que vous avez rentré n'est pas valide")
        pass
    print ("_ " * 50)

SystemExit

"""
"""
from pathlib import *

p = Path.home()      #C:\ Users\ nathan.dubroc
print(p)

p = Path.cwd()       #C:\Users\ nathan.dubroc
print(p)

w = p / "Documents"  #C:\ Users\ nathan.dubroc\Documents
print(w) 

j = p / "data.json"  #C:\ Users\ nathan.dubroc\data.json
print (j)

s = j.suffix         # Ca donne le type de fichier => donc ici .json
print(s)

print(j.name)        #Le nom du dernier element => data.json
print(j.parent)      #C:\ Users\ nathan.dubroc\ 
print(j.stem)        #Donne le nom visible ici => data
print(j.suffix)      #Donne le suffix ici=> .json
print(j.suffixes)    #Donne sous forme de liste tout les suffixe si il ya un fichier sous un format xxx.yy.zz ["yy", "zz"]
print(j.parts)       #Donne sous forme de tuple => ("\ ", "User", "nathan.dubroc", "data.json")
print(j.exists())    #Booleen et verifie si il existe
print(j.is_dir())    #Booleen et verifie si c'est un dossier
print(j.is_file())   #Booleen et verifie si c'est un fichier

print(p.parent.parent)  #On peut ici concatener les fonctions psk p est un objet 
"""


from pathlib import *

dir = {".png" : "Images",      #Dictionnaire où on associe un type de fichier à un nom de Dossiers
       ".jpeg" : "Images",
       ".mp4" : "Videos",
       ".zip" : "Archives",
       ".pdf" : "Documents",
       }

Tri_dir = Path.home() / "Tri"    #"On indique dans quel Dossier on veut effectuer le tri"
files = [ f for f in Tri_dir.iterdir() if f.is_file() ]   #On récupère uniquement les fichiers contenu dans celui ci et non les dossiers
for f in files :                                          #On créer une boucles avec tout les fichers
    output_dir = Tri_dir / dir.get(f.suffix, "Autres")    #Si un type de fichier n'est pas pris en compte on le lie à un nouveau dossier (Autres)
    output_dir.mkdir(exist_ok=True)                       #On créer le dossier correspondant en respectant la condition qu'il n'existe déjà pas
    f.rename(output_dir / f.rename)                       #On redirige les fichiers vers les dossiers choisis et crée

 


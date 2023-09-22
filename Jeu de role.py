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

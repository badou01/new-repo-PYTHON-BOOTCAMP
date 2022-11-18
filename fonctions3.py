import random
def debut_partie(n :int):
    print('Partie ',n)
    print('Bienvenu dans le jeu LET-GET')
    print('#####################################')
    print('Vous avez 3 point-erreur')
    print('#####################################')
    print('Vous avez 6 tentatives')
    print('#####################################')
    print()
    print(" +---+")
    print(" |   |")
    print(" |    ")
    print(" |      ")
    print(" |      ")
    print("_|_")
    print("| |")




def charger_niveau():
	a=input('Choisir un niveau de 1 a 3: \n ')
	while(a != '1' and a != '2' and a != '3' and a != '4' and a != '5' 		 and a != '6' and a != '7' and a != '8' and a != '9' and a != '0'):
		print(('Veuillez entrez une chiffre'))
		a = input('Choisir un niveau de 1 a 3: \n ')
	a=int(a)
	while(a>3 or a<1):
		print('Entrer un nombre compris entre 1 et 3!')
		a = input('Choisir un niveau de 1 a 3: \n ')
	print('###################################')
	print('Vous avez choisi le niveau ',a)
	return a
def mots_pour_niveau(a : int):
    # commentaires de specifications
    with open('mots.txt', 'r') as mon_fichier:
        texte_entier=mon_fichier.read()
        mots= list(map(str, texte_entier.split()))

        tak_tak = random.choice(mots)

    chargement = niveau()
    if(a==1):
        print(len(chargement[0]), " mots charges")
        while(len(tak_tak)>4 or len(tak_tak)<2):
            tak_tak = random.choice(mots)
        return tak_tak
    if(a==2):
        print(len(chargement[1]), " mots charges")
        while (len(tak_tak) > 7 or len(tak_tak )< 5):
            tak_tak = random.choice(mots)
        return tak_tak
    if (a == 3):
        print(len(chargement[2]), " mots charges")
        while (len(tak_tak )<= 7):
            tak_tak = random.choice(mots)
        return tak_tak
#fin fonction mots_pour_niveau()

def niveau():
    niveau1 = []
    niveau2 = []
    niveau3 = []
    with open("mots.txt") as mo:
        for m in mo:
            if len(m) < 5:
                niveau1.append(m.rstrip("\n"))
            elif (len(m) > 4) and (len(m) < 8):
                niveau2.append(m.rstrip("\n"))
            else:
                niveau3.append(m.rstrip("\n"))
    return niveau1, niveau2, niveau3

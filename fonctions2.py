from fonctions3 import  *
from pendule import *
def debut_saisie(mot_genere):

    print('Je vous propose un mot de', len(mot_genere), ' lettres. De quel mot s’agit-il ? ')
    print('################################')
    print('')
    print('_  ' * len(mot_genere))

def saisie_lettre(mot_genere,tentatives=6,point_erreurs=3,id_partie=0,inconnu=''):
        if(inconnu==''):
            inconnu = ['_'] * len(mot_genere)

        letter = input('Saisir une lettre: ')

        while (len(letter) > 1 or letter.isalpha() == False):
            print('On a dit une lettre. Quand meme')
            point_erreurs -= 1
            print('Il vous reste ', point_erreurs, ' avertissements')

            if (point_erreurs == 0):
                tentatives -= 1
                print('vous perdez une tentative')
                print('il vous reste ', tentatives, ' tentatives')
            letter = str(input('Saisir une lettre: '))
        return mot_genere,letter,tentatives,point_erreurs,inconnu,id_partie


def check_lettre(mot_genere,letter,tentatives :int,point_erreurs :int,inconnu,id_partie,avertissement=3,max=0):
    if(letter not in inconnu):
        if (letter in mot_genere):
            occur_letter = 0
            print('Bravo, lettre correcte')
            if(tentatives<6):
             print("Vous avez gagne une tentative de plus")
            for i in range(len(mot_genere)):
                if (mot_genere[i] == letter):
                    occur_letter += 1
                    inconnu.pop(i)
                    inconnu.insert(i, letter)
                    # si on trouve un autre mot il ne l'ajoute pas
            for b in range(len(inconnu)):
                print(inconnu[b], end=' ')
            if (tentatives < 6):
                tentatives += 1
        else:
            grpe = verif_type_lettre(letter, tentatives, inconnu, id_partie)
            tentatives = grpe[0]
            inconnu = grpe[1]
    else:
        print('Lettre déjà trouvé.')
        avertissement -= 1
        print("Il vous reste {} avertissement.".format(avertissement))
        if(avertissement == 0):

            tentatives -= 1
            avertissement = 3
        print('#######################################')
        print(' Il vous reste ', tentatives, ' tentatives')
        print('#######################################')
        for b in range(len(inconnu)):
            print(inconnu[b], end=' ')
    while((tentatives > 0) and inconnu != list(mot_genere)):
        op=saisie_lettre(mot_genere,tentatives,point_erreurs,id_partie,inconnu)
        check_lettre(op[0],op[1],op[2],op[3],op[4],op[5],avertissement)
    gagner_ou_perdre(tentatives,inconnu,mot_genere,id_partie,max)

#fin check_lettre()
def verif_type_lettre(letter,tentatives :int,inconnu,id_partie):
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y'):
        print('Vous avez saisi une voyelle qui n\'est pas dans le mot.')
        print('Vous perdez deux tentatives')
        # k=tentatives
        tentatives -= 2
        if tentatives < 0:
            tentatives = 0
        print('#######################################')
        print(' Il vous reste ', tentatives, ' tentatives')
        print('#######################################')
        pendule(tentatives)
        for b in range(len(inconnu)):
            print(inconnu[b],end=' ')
    else:
        print('Vous avez saisi une consonne qui n\'est pas dans le mot.')
        tentatives -= 1
        if tentatives < 0:
            tentatives = 0
        print('Vous perdez une tentative.')
        print('#######################################')
        print('Il vous reste ', tentatives, ' tentatives')
        print('#######################################')
        pendule(tentatives)
        for b in range(len(inconnu)):
            print(inconnu[b],end=' ')
    return tentatives,inconnu,id_partie

def gagner_ou_perdre(tentatives :int,inconnu,mot_genere,id_partie: int, score: int,max=0):

    if (tentatives == 0 ):
        if inconnu != list(mot_genere):
            print('\nechec! Vous avez perdu.c\'etait: ',mot_genere)
            print('________________________________________')
        else:

            print("Bravo! Vous avez gagne. c'etait {}.".format(mot_genere))
            score = len(set(mot_genere))
            print("Votre score : {}".format(tentatives * score))
            if(id_partie==1):
                max=tentatives*score
            elif(id_partie>1):
                if((tentatives*score)>max):
                    max=tentatives*score

            log = open("log_game.txt","a")
            ab=f'\nPartie: ,{id_partie}, \nNombre de tentative:, {tentatives}, \nScore obtenu: , {tentatives * score}, \nScore max:  {max}'
            log.write(ab)
            log.close()

    else:
        if inconnu == list(mot_genere):
            print('\nBravo! Vous avé gagné.c\'etait: ', mot_genere)
            score = len(set(mot_genere))
            print("Votre score : {}".format(tentatives * score))
            if (id_partie == 1):
                max = tentatives * score
            elif (id_partie > 1):
                if ((tentatives * score) > max):
                    max = tentatives * score
            log = open("log_game.txt", "a")
            ab=f'Partie: ,{id_partie}, \nNombre de tentative:, {tentatives}, \nScore obtenu: , {tentatives * score}, \nScore max:  {max}'
            log.write(ab)
            log.close()

    suite = input('Voulez vouz faire une autre partie?1-OUI,0-NON')
    while(suite!='0' and suite!='1'):
        print('entrer soit zero soit un')
        suite = input('Voulez vouz faire une autre partie?')
    if(suite=='1'):
        id_partie+=1
        test_function(id_partie,max)
    elif(suite=='0'):
        print('bye! a la prochaine')
        quit()

#-------------------------------------------------------------------------------------------------------------

def test_function(id_partie: int,max ):
    tentatives,point_erreurs=6,3
    debut_partie(id_partie)
    mot_genere=mots_pour_niveau(charger_niveau())
    debut_saisie(mot_genere)

    var_saisie=saisie_lettre(mot_genere,tentatives,point_erreurs,id_partie)
    check_lettre(var_saisie[0], var_saisie[1], var_saisie[2], var_saisie[3], var_saisie[4], var_saisie[5],max)

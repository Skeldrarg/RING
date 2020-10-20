import personnages
import capacites
import os
import time

def ecran_titre():
    print("\
     _____  _____ _   _  _____\n\
    |  __ \|_   _| \ | |/ ____|\n\
    | |__) | | | |  \| | |  __\n\
    |  _  /  | | | . ` | | |_ |\n\
    | | \ \ _| |_| |\  | |__| |\n\
    |_|  \_\_____|_| \_|\_____|")
    time.sleep(2)

def choix_perso():
    dico_persos = {'1':personnages.Warrior,'2':personnages.Mage,'3':personnages.Thief}
    choix = input("Choisissez votre classe\n------------------------\n\
1. Guerrier\n2. Mage\n3. Voleur\n\n")
    os.system('cls||clear')
    perso = dico_persos[choix]()
    perso.setStats()
    perso.setVitality()
    #print(perso)
    return perso

def choix_capacite(perso):
    os.system("clear||cls")
    dico_capacites = {'1':capacites.Capacite("Epée","IMP","PAR","MAN"),\
                  '2':capacites.Capacite("Bouclier","MAN","PRO"),\
                  '3':capacites.Capacite("Sort d'attaque","FAC","EFF"),\
                  '4':capacites.Capacite("Sort de défense","FAC","EFF"),\
                  '5':capacites.Capacite("Potion","FAC","EFF"),\
                  '6':capacites.Capacite("Sort de soin","FAC","EFF")}
    choix = input("Choisissez une capacité pour {0}\n1. Epée\n2. Bouclier\n3. Sort d'attaque\n4. Sort de défense\n5. Potion\n6. Sort de soin\n\n".format(perso.name))
    capacite = dico_capacites[choix]
    capacite.setStats()
    perso.CAPACITES.append(capacite)

def creation_personnage():
    perso = choix_perso()
    if perso.EXP / 2 < 2:
        for i in range(2):
            choix_capacite(perso)
    else:
        for i in range(int(perso.EXP / 2) - 1):
            choix_capacite(perso)
    return perso
import tests
import menus
import os

def init_duel():
    print("Joueur 1 créez votre personnage\n")
    p1 = menus.creation_personnage()
    os.system("clear||cls")
    print("Joueur 2 créez votre personnage\n")
    p2 = menus.creation_personnage()
    return p1, p2

def duel(p1, p2):
    pass


def main():
    #menus.ecran_titre()
    #os.system("clear||cls")
    #p1, p2 = init_duel()
    #duel(p1, p2)
    tests.testStatsPersos()


if __name__ == "__main__":
    main()
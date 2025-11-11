DEBUG = True
from random import *
from collections import deque

VALEURS = ['','', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
COULEURS = ['', 'H', 'S', 'D', 'C']
# H=coeur, S=pique, D=carreau, C=trefle, J=valet, Q=reine, K=roi, A=As


class Carte:
    """Initialise couleur (de 1 à 4), et valeur (de 2 à 14)"""

    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
        return VALEURS[self.valeur]

    def get_couleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
        return COULEURS[self.couleur]

    def Nom_cartes(self):
        return self.get_nom() + self.get_couleur()

    def __str__(self):
        return self.Nom_cartes()

    #less than → lt
    def __lt__(self, other):
        return self.Nom_cartes() < other.Nom_cartes()

    #greater than → gt
    def __gt__(self, other):
        return self.Nom_cartes() > other.Nom_cartes()

    #equal to → eq
    def __eq__(self, other):
        return self.Nom_cartes() == other.Nom_cartes()


class file:

    def __init__(self):
        self.table_f = deque()

    #enfile
    def enfile(self, c):
        return self.table_f.append(c)

    #defile
    def defile(self):
        if not self.estVide():
            return self.table_f.popleft()

    #len -> nombre cartes
    def longueur(self):
        return len(self.table_f)

    #verifier si la file est vide (renvoie True si elle est vide sinon False)
    def estVide(self):
        return len(self.table_f) == 0

    #regarder dessus
    def regarder(self):
        return self.table_f[-1]

    def __str__(self):
        s = ""
        for c in self.table_f:
            s += str(c) + " "
        return s


class pile:

    def __init__(self):
        self.table_p = []

    #empile
    def empile(self,c):
        return self.table_p.append(c)

    #depile
    def depile(self):
        if not self.estVide():
            return self.table_p.pop()

    #nombre cartes
    def longueur(self):
        return len(self.table_p)

    #verifier si la pile est vide (renvoie True si elle est vide sinon False)
    def estVide(self):
        return len(self.table_p) == 0

    #regarder
    def regarder(self):
        return self.table_p[-1]

    def __str__(self):
        s = ""
        for c in self.table_p:
            s += str(c) + " "
        return s


class PaquetDeCarte:
    """Initialise un paquet de cartes, avec un attribut contenu, de type list, vide"""

    def __init__(self):
        self.contenu = []
        self.remplir()
        self.melanger()
        self.afficher()

    def remplir(self):
        """Remplit le paquet de cartes : en parcourant les couleurs puis les valeurs"""
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]

    def get_carte_at(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        if 0 <= pos < 52:
            return self.contenu[pos]

    #melanger le jeu de cartes
    def melanger(self):
        shuffle(self.contenu)

    #afficher les cartes
    def afficher(self):
        for carte in self.contenu:
            print(carte.Nom_cartes())


class Partie_bataille():

    def __init__(self):
        self.J1 = file()
        self.J2 = file()
        self.p = PaquetDeCarte()
        self.tapis1 = pile()
        self.tapis2 = pile()

    #Distribuer les cartes
    def distribuer_cartes(self):
        for i in range (len(self.p.contenu)): #Si on veut voir qui gagne jusqu'à la fin, on modifie le code dans une boucle par exemple si on met 10 dans une boucle, elle distribue 5 cartes à chacun joueurs(file).
            if i%2 == 0:
                self.J1.enfile(self.p.contenu[i])
            else:
                self.J2.enfile(self.p.contenu[i])

        if(DEBUG):
            print(self.J1)
            print(self.J2)

    #Jouer le jeu
    def parties(self):
        #tant que le jeu 1 n’est pas vide ou le jeu 2 n’est pas vide faire, mettre au tapis
        while not (self.J1.estVide() or self.J2.estVide()):
            self.tapis1.empile(self.J1.defile())
            self.tapis2.empile(self.J2.defile())

            if(DEBUG):
                print(str(self.tapis1))
                print(str(self.tapis2))

            #tant que les 2 cartes du dessus des piles du tapis sont  égales faire
            while self.tapis1.regarder() == self.tapis2.regarder():
                if(DEBUG):
                    print("Égalité !")
                #Tirer 2 fois une carte du paquet de J1 sur le tapis
			    #Tirer 2 fois une carte du paquet de J2 sur le tapis
                for _ in range(2):
                    self.tapis1.empile(self.J1.defile())
                    self.tapis2.empile(self.J2.defile())

                if(DEBUG):
                    print(str(self.tapis1))
                    print(str(self.tapis2))

            #J1 gagne tant que le jeu 1 n'est pas vide
            if self.tapis1.regarder() > self.tapis2.regarder():
                while not self.tapis1.estVide():
                    self.J1.enfile(self.tapis1.depile())
                while not self.tapis2.estVide():
                    self.J1.enfile(self.tapis2.depile())
                if(DEBUG):
                    print("Joueur 1 a gagné !")
            #J2 gagne tant que je le jeu 2 n'est pas vide
            else:
                while not self.tapis1.estVide():
                    self.J2.enfile(self.tapis1.depile())
                while not self.tapis2.estVide():
                    self.J2.enfile(self.tapis2.depile())
                if(DEBUG):
                    print("Joueur 2 a gagné !")

            if(DEBUG):
                print(str(self.J1))
                print(str(self.J2))

        #Gagnant du jeu
        gagnant = "Joueur 1" if self.J2.estVide() else "Joueur 2"
        if(DEBUG):
            print(f"Le gagnant est {gagnant} !")


pb=Partie_bataille()
pb.distribuer_cartes()
pb.parties()
jeu = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

def afficher_plateau(jeu):
    for i in range(len(jeu)):
        print(jeu[i])

#print(afficher_plateau(jeu))


def jouer(jeu, joueur):
    mot = input("Quelle colonne veux-tu jouer ? (0, 1 ou 2) :")
    mot2 = input("Quelle ligne veux-tu jouer ? (0, 1 ou 2) :")
    jeu[int(mot2)][int(mot)] = joueur

#print(jouer(jeu, 'O'))

def verifier_victoire(jeu):
        if jeu[0][0] == jeu[1][1] == jeu[2][2] != '.':
            return True # Victoire sur la diagonale
        if jeu[0][2] == jeu[1][1] == jeu[2][0] != '.':
            return True # Victoire sur l'autre diagonale
        if jeu[0][0] == jeu[0][1] == jeu[0][2] !='.':
            return True # Victoire sur la premiere ligne horizontale
        if jeu[1][0] == jeu[1][1] == jeu[1][2] !='.':
            return True # Victoire sur la deuxieme ligne horizontale
        if jeu[2][0] == jeu[2][1] == jeu[2][2] !='.':
            return True # Victoire sur la troisieme ligne horizontale
        if jeu[0][0] == jeu[1][0] == jeu[2][0] != '.':
            return True # Victoire sur la premiere ligne verticale
        if jeu[0][1] == jeu[1][1] == jeu[2][1] != '.':
            return True # Victoire sur la deuxieme ligne verticale
        if jeu[0][2] == jeu[1][2] == jeu[2][2] != '.':
            return True # Victoire sur la troisieme ligne verticale
        return False

#print(verifier_victoire(jeu))


def changer_joueur(joueur):
    for i in joueur:
        if i == 'O':
            return 'X'
        elif i == 'X':
            return 'O'
        None
        
#print(changer_joueur("."))


#Écriture de l’algorithme

afficher_plateau(jeu)
joueur = 'X'
gagne = False
while gagne == False:
    print("Au tour de", joueur)
    jouer(jeu, joueur)
    afficher_plateau(jeu)
    if verifier_victoire(jeu):
        gagne = True
        print("Le joueur", joueur, "a gagné !")
    else:
        joueur = changer_joueur(joueur)




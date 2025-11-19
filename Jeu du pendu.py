def lettre_dans_liste(lettre, solution, reponse): # (ex.: ('a', ['c','h','a','t'], ['_','_','_','_']))
    bonne_lettre = False
    for i in range(len(solution)):
        if solution[i] == lettre: # Si la lettre saisie par joueur est dans mot, (ex.: solution[2]='a'=='a')
            reponse[i] = lettre  # On positionne cette lettre dans la liste reponse en même indice que solution. (ex.: ['_','_','a','_'])
            bonne_lettre = True
    return bonne_lettre


def pendu():
    mot = input("Tapez un mot : ") # Demande au joueur pour saisir un mot
    solution = list(mot) # Liste de mot (ex.: chat -> ['c','h','a','t'])
    reponse = ["_"] * len(mot) # (ex.: ['_','_','_','_'])
    c = 20 # Vies

    print("\n" * 30) # Pour ne pas montrer au joueur qui cherche le mot
    print("Le jeu du pendu commence !\n")

    while c > 0:
        print("Mot :", " ".join(reponse)) # On affiche les tirets bas vides en fonction de la taille de mot
        print(f"Vies restantes : {c}") # On affiche les vies
        lettre = input("Tapez une lettre : ") # Demande au joueur pour saisir une lettre

        if lettre in reponse: # Si joueur a saisi la bonne lettre qu'il a déjà saisi, 
            print("Lettre déjà utilisée.\n")
            continue

        if lettre_dans_liste(lettre, solution, reponse): # Appel de fonction 
            print("Bonne lettre !\n")
        else:
            c -= 1 # On réduit la vie
            print("Mauvaise lettre.\n")

        if reponse == solution: # Si le joueur a réussi à trouver le mot
            print("Gagné ! Le mot était :", mot)
            return # Fin de fonction pendu()

    print("Perdu ! Le mot était :", mot)


pendu()

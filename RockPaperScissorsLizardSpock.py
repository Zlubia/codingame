import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

Liste_joueurs = []
Dictionnaire_Gagnants = {}
n = int(input())
for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]

    combo_joueur = (numplayer,signplayer)
    Liste_joueurs.append(combo_joueur)
    Dictionnaire_Gagnants[i+1] = [0]

print(n, file=sys.stderr, flush=True)
print(Liste_joueurs, file=sys.stderr, flush=True)
print(Dictionnaire_Gagnants, file=sys.stderr, flush=True)

i = 0
j = n
vainqueur = ()
perdant = ()
Liste_perdants = []
string_vaincus = ""

def match(Joueur_gauche, Joueur_droit):
    global vainqueur, perdant
    #print("fonction - joueur gauche", Joueur_gauche)
    #print("fonction - joueur droit", Joueur_droit)
    if Joueur_gauche[1] == "C" or Joueur_droit[1] == "C" :
        #joueur_gauche gagne
        if Joueur_gauche[1] == "C" and Joueur_droit[1] == "P":

            vainqueur = Joueur_gauche
            perdant = Joueur_droit    
            
        elif Joueur_gauche[1] == "C" and Joueur_droit[1] == "S":
            vainqueur = Joueur_droit
            perdant = Joueur_gauche

        elif Joueur_gauche[1] == "C" and Joueur_droit[1] == "L":
            vainqueur = Joueur_gauche
            perdant = Joueur_droit 

        elif Joueur_gauche[1] == "C" and Joueur_droit[1] == "R":
            vainqueur = Joueur_droit
            perdant = Joueur_gauche
        
        #inversion
        elif Joueur_droit[1] == "C" and Joueur_gauche[1] == "P":

            vainqueur = Joueur_droit
            perdant = Joueur_gauche    
            
        elif Joueur_droit[1] == "C" and Joueur_gauche[1] == "S":
            vainqueur = Joueur_gauche
            perdant = Joueur_droit

        elif Joueur_droit[1] == "C" and Joueur_gauche[1] == "L":
            vainqueur = Joueur_droit
            perdant = Joueur_gauche 

        elif Joueur_droit[1] == "C" and Joueur_gauche[1] == "R":
            vainqueur = Joueur_gauche
            perdant = Joueur_droit
            
        else :
            #le joueur avec le chiffre le plus élevé est le vainqueur
            if Joueur_gauche[0] < Joueur_droit[0] :
                vainqueur = Joueur_gauche
                perdant = Joueur_droit
            
            else :
                vainqueur = Joueur_droit
                perdant = Joueur_gauche

    elif Joueur_gauche[1] == "R" or Joueur_droit[1] == "R" :
        #joueur_gauche gagne
        if Joueur_gauche[1] == "R" and Joueur_droit[1] == "L":

            vainqueur = Joueur_gauche
            perdant = Joueur_droit    
            
        elif Joueur_gauche[1] == "R" and Joueur_droit[1] == "P":
            vainqueur = Joueur_droit
            perdant = Joueur_gauche

        elif Joueur_gauche[1] == "R" and Joueur_droit[1] == "S":
            vainqueur = Joueur_droit
            perdant = Joueur_gauche
        #inversion
        elif Joueur_droit[1] == "R" and Joueur_gauche[1] == "L":

            vainqueur = Joueur_droit
            perdant = Joueur_gauche  
            
        elif Joueur_droit[1] == "R" and Joueur_gauche[1] == "P":
            vainqueur = Joueur_gauche
            perdant = Joueur_droit

        elif Joueur_droit[1] == "R" and Joueur_gauche[1] == "S":
            vainqueur = Joueur_gauche
            perdant = Joueur_droit

        else :
            #le joueur avec le chiffre le plus élevé est le vainqueur
            if Joueur_gauche[0] < Joueur_droit[0] :
                vainqueur = Joueur_gauche
                perdant = Joueur_droit
            
            else :
                vainqueur = Joueur_droit
                perdant = Joueur_gauche
            
    elif Joueur_gauche[1] == "P" or Joueur_droit[1] == "P" :
        #joueur_gauche gagne
        if Joueur_gauche[1] == "P" and Joueur_droit[1] == "S":

            vainqueur = Joueur_gauche
            perdant = Joueur_droit
            
        elif Joueur_gauche[1] == "P" and Joueur_droit[1] == "L":
            vainqueur = Joueur_droit
            perdant = Joueur_gauche
        #inversion
        elif Joueur_droit[1] == "P" and Joueur_gauche[1] == "S":

            vainqueur = Joueur_droit
            perdant = Joueur_gauche
            
        elif Joueur_droit[1] == "P" and Joueur_gauche[1] == "L":
            vainqueur = Joueur_gauche
            perdant = Joueur_droit
        

        else :
            #le joueur avec le chiffre le plus élevé est le vainqueur
            if Joueur_gauche[0] < Joueur_droit[0] :
                vainqueur = Joueur_gauche
                perdant = Joueur_droit
            
            else :
                vainqueur = Joueur_droit
                perdant = Joueur_gauche   

    elif Joueur_gauche[1] == "L" or Joueur_droit[1] == "L" :
        #joueur_gauche gagne
        if Joueur_gauche[1] == "L" and Joueur_droit[1] == "S":

            vainqueur = Joueur_gauche
            perdant = Joueur_droit
        #inversion
        elif Joueur_droit[1] == "L" and Joueur_gauche[1] == "S":

            vainqueur = Joueur_droit
            perdant = Joueur_gauche

        else :
            #le joueur avec le chiffre le plus élevé est le vainqueur
            if Joueur_gauche[0] < Joueur_droit[0] :
                vainqueur = Joueur_gauche
                perdant = Joueur_droit
            
            else :
                vainqueur = Joueur_droit
                perdant = Joueur_gauche   
    else :
        #Joueur_Gauche et joueur droit ont S
            if Joueur_gauche[0] < Joueur_droit[0] :
                vainqueur = Joueur_gauche
                perdant = Joueur_droit
            
            else :
                vainqueur = Joueur_droit
                perdant = Joueur_gauche

    return vainqueur, perdant




while j > 1 :
    #combat en cours

    match(Liste_joueurs[i], Liste_joueurs[i+1])

    print("vainqueur", vainqueur, file=sys.stderr, flush=True)
    print("perdant", perdant, file=sys.stderr, flush=True) 

    #encoder dans un dictionnaire le numéro du gagnant avec celui du perdant. la clé c'est le gagnant et 
    #la valeur sera une liste des perdants
    numero_gagnant = vainqueur[0]
    numero_perdant = perdant[0]

    #print(" ")
    #print("numero vainqueur", numero_gagnant)
    #print("numero perdant", numero_perdant) 

    #récuperer la liste des numéros perdants qui correspond au numéro gagnant
    Liste_perdants = Dictionnaire_Gagnants.get(vainqueur[0])
    #y ajouter le nouveau perdant
    
    #print("liste du perdant", Liste_perdants)

    Liste_perdants.append(perdant[0])
    
    #print("liste du perdant completée", Liste_perdants)

    Dictionnaire_Gagnants[vainqueur[0]] = Liste_perdants

    #print("dictionnaire", Dictionnaire_Gagnants)

    #Retirer le tuple perdant de la liste des joueurs

    if perdant == Liste_joueurs[i] :
        del Liste_joueurs[i]
    else :
        del Liste_joueurs[i+1]

    print(Liste_joueurs, file=sys.stderr, flush=True)
    print(" ", file=sys.stderr, flush=True)
    print(" ", file=sys.stderr, flush=True)


    #itération de i (qui sert à selectionner les tuples dans la liste)
    i += 1

    #réinitialiser i à la fin d'un round
    if i == len(Liste_joueurs) :
        i = 0
    
    j = len(Liste_joueurs)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



#Voici le Gagnant
Gagnant = Liste_joueurs[0]
print(Gagnant[0])

#sortir la liste des vaincus

Liste_vaincus = Dictionnaire_Gagnants.get(Gagnant[0])

del Liste_vaincus[0]
#print(Liste_vaincus)

vaincus = ' '.join(str(element) for element in Liste_vaincus)

print(vaincus)

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

b = input()
length_string = len(b)
print(length_string, file=sys.stderr, flush=True)
print(b, file=sys.stderr, flush=True)

liste_d_index = []

longest_streak = 0

index = 0


while index < length_string :
    #chercher les 0 solitaires dans la liste. Tout les 0 entourés de 1
    #print(b[index], file=sys.stderr, flush=True)

    if index == length_string - 1 :
        #exception pour la dernière case de la liste
        if b[index] == '0' and b[index-1] == '1' :
            #print("cest un zero " + b[index], file=sys.stderr, flush=True)
            liste_d_index.append(index)

    elif index == 0 :
        #exception pour la première case de la liste
        if b[index] == '0' and b[index+1] == '1' :
            #print("cest un zero " + b[index], file=sys.stderr, flush=True)
            liste_d_index.append(index)

    elif b[index] == '0' and (b[index-1] == '1' or b[index+1] == '1' ):
        #print("cest un zero " + b[index], file=sys.stderr, flush=True)
        liste_d_index.append(index)

    index += 1


if len(liste_d_index) == 0 :

    longest_streak = 1
    
else :
    for i in liste_d_index :
        #on remplace chaque fois un des 0 par un 1
        #print(i, file=sys.stderr, flush=True)

        bitstring_provisoire = list(b)

        #print(bitstring_provisoire, file=sys.stderr, flush=True)

        bitstring_provisoire[i] = '1'

        #print(bitstring_provisoire, file=sys.stderr, flush=True)

        bit = 0
        streak = 0

        while bit < length_string :
        # on parcours la liste en comptant la plus longue string de 1

            if bitstring_provisoire[bit] == '1':
                streak += 1

            elif bitstring_provisoire[bit] == '0' :

                streak = 0

            if streak > longest_streak :
                longest_streak = streak

            bit += 1

            #print(longest_streak, file=sys.stderr, flush=True)
                
           



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("longest streak is", file=sys.stderr, flush=True)

print(longest_streak)

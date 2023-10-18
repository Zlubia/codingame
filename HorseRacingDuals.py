import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

horse_list = []
smallest_strength_gap = None


n = int(input())
for i in range(n):
    pi = int(input())
    horse_list.append(pi)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

"""
Avant tout nous allons mettre les listes dans l'ordre croissant, ainsi on ne devra comparer que les chevaux voisins
On utilise la fonction sort de python (O(n log n))
"""
horse_list.sort()

print(horse_list, file=sys.stderr, flush=True)

i = 0

while i < len(horse_list)-1 :

    strength_gap = horse_list[i+1] - horse_list[i]
    i += 1
    
    if  smallest_strength_gap == None or strength_gap < smallest_strength_gap :

        smallest_strength_gap = strength_gap

print(smallest_strength_gap

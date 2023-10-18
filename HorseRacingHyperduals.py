import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

distance_min = None
horse_list = []

n = int(input())
for i in range(n):
    v, e = [int(j) for j in input().split()]
    horse_list.append((v,e))

#print("Distance...", horse_list, file=sys.stderr, flush=True)

i = 0


while i < len(horse_list) :

    j = 0
    #print("i is : " , i, file=sys.stderr, flush=True)

    while j < len(horse_list) :

        #print("j is : " , j, file=sys.stderr, flush=True)

        if i != j :
        
            #print("horse_list[i][0] is : " , horse_list[i][0], file=sys.stderr, flush=True)
            #print("horse_list[j][0] is : " , horse_list[j][0], file=sys.stderr, flush=True)

            #print("horse_list[i][1] is : " , horse_list[i][1], file=sys.stderr, flush=True)
            #print("horse_list[j][1] is : " , horse_list[j][1], file=sys.stderr, flush=True)

            #print("calcul is : " , horse_list[i][1]-horse_list[j][1], file=sys.stderr, flush=True)
            
            distance = abs(horse_list[i][0]-horse_list[j][0]) + abs(horse_list[i][1] - horse_list[j][1])
            #print("Distance...", distance, file=sys.stderr, flush=True)

            if distance_min == None or distance < distance_min :
                distance_min = distance
        j += 1
    i +=1
        
if distance_min == None :
    distance_min = 0



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(distance_min)

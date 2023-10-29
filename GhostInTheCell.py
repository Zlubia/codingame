import sys
import math

#Initialize variables
list_of_distances = []
Turn_count = 0

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

factory_count = int(input())  # the number of factories
link_count = int(input())  # the number of links between factories

for i in range(link_count):
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    list_of_distances.append((factory_1, factory_2, distance))
   


#-----------FUNCTIONS--------------------

def verify_distance(factory_1, factory_2):
    """
    Function pour trouver la distance entre 2 usines.
    Return distance
    """

    if factory_1 < factory_2 :
        for j in list_of_distances :
            if j[0] == factory_1 and j[1] == factory_2 :
                distance = j[2]
    else :
        for j in list_of_distances :
            if j[0] == factory_2 and j[1] == factory_1 :
                distance = j[2]

    return distance

# game loop
while True:
    Turn_count += 1

    production_3_neutral = []
    production_2_neutral = []
    production_1_neutral = []
    production_0_neutral = []

    production_3_enemy = []
    production_2_enemy = []
    production_1_enemy = []
    production_0_enemy = []

    max_cyborgs = 0


    entity_count = int(input())  # the number of entities (e.g. factories and troops)

    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])

        if entity_type == "FACTORY" :
            if arg_1 == 0 : #If the factory is neutral
                if arg_3 == 3 : #if production is 3
                    production_3_neutral.append(i)
                elif arg_3 == 2 :
                    production_2_neutral.append(i)
                elif arg_3 == 1 :
                    production_1_neutral.append(i)
                elif arg_3 == 0 :
                    production_0_neutral.append(i)

            if arg_1 == -1 : #If the factory is an enemy
                if arg_3 == 3 : #if production is 3
                    production_3_enemy.append(i)
                elif arg_3 == 2 :
                    production_2_enemy.append(i)
                elif arg_3 == 1 :
                    production_1_enemy.append(i)
                elif arg_3 == 0 :
                    production_0_enemy.append(i)

            if arg_1 == 1 : #If it's my factory
                if arg_2 > max_cyborgs :
                    max_cyborgs = arg_2
                    factory_max_cyborgs = i
                    print("max_cyborgs : ", max_cyborgs, file=sys.stderr, flush=True)
                    print("factory_max_cyborgs : ", factory_max_cyborgs, file=sys.stderr, flush=True)

    """
    Trouver la distance la plus petite parmis les factorys
    """

    if len(production_3_neutral) > 0 :
        closest_factory_3 = (-1, 50000)

        for i in production_3_neutral :
            distance = verify_distance(factory_max_cyborgs, i)
            if distance < closest_factory_3[1] :
                closest_factory_3 = (i, distance)
        
    else :
        closest_factory_3 = ()

    if len(production_2_neutral) > 0 :
        closest_factory_2 = (-1, 50000)
        for i in production_2_neutral :
            distance = verify_distance(factory_max_cyborgs, i)
            if distance < closest_factory_2[1] :
                closest_factory_2 = (i, distance)
    else :
        closest_factory_2 = ()

    if len(production_1_neutral) > 0 :
        closest_factory_1 = (-1, 50000)
        for i in production_1_neutral :
            distance = verify_distance(factory_max_cyborgs, i)
            if distance < closest_factory_1[1] :
                closest_factory_1 = (i, distance)
    else :
        closest_factory_1 = ()

    if len(production_0_neutral) > 0 :
        closest_factory_0 = (-1, 50000)
        for i in production_0_neutral :
            distance = verify_distance(factory_max_cyborgs, i)
            if distance < closest_factory_0[1] :
                closest_factory_0 = (i, distance)
    else :
        closest_factory_0 = ()

    #Une fois toutes les factory neutres prises, on attaque les ennemis :

    if len(closest_factory_3) == 0 and len(closest_factory_2) == 0 and len(closest_factory_1) == 0 and len(closest_factory_0) == 0 :
        if len(production_3_enemy) > 0 :
            closest_factory_3 = (-1, 50000)

        for i in production_3_enemy :
            distance = verify_distance(factory_max_cyborgs, i)
            if distance < closest_factory_3[1] :
                closest_factory_3 = (i, distance)
        
        else :
            closest_factory_3 = ()

        if len(production_2_enemy) > 0 :
            closest_factory_2 = (-1, 50000)
            for i in production_2_enemy :
                distance = verify_distance(factory_max_cyborgs, i)
                if distance < closest_factory_2[1] :
                    closest_factory_2 = (i, distance)
        else :
            closest_factory_2 = ()

        if len(production_1_enemy) > 0 :
            closest_factory_1 = (-1, 50000)
            for i in production_1_enemy :
                distance = verify_distance(factory_max_cyborgs, i)
                if distance < closest_factory_1[1] :
                    closest_factory_1 = (i, distance)
        else :
            closest_factory_1 = ()

        if len(production_0_enemy) > 0 :
            closest_factory_0 = (-1, 50000)
            for i in production_0_enemy :
                print("i : ", i, file=sys.stderr, flush=True)
                distance = verify_distance(factory_max_cyborgs, i)
                if distance < closest_factory_0[1] :
                    closest_factory_0 = (i, distance)
        else :
            closest_factory_0 = ()
   
    
    """
    Définir vers quelle factory envoyer (mélange entre production élevé et distance courte)
    """

    if len(closest_factory_3) > 0 :

        closest_factory = closest_factory_3

        if len(closest_factory_2) > 0 :
            distance_delta = closest_factory_3[1] - closest_factory_2[1]
            if distance_delta > 2 : #le 2 est le nombre de tour de production. En 2 tours, un factory 2 produit 4 cyborgs.
                closest_factory = closest_factory_2
        
        if len(closest_factory_1) > 0 and closest_factory == closest_factory_3:
            distance_delta = closest_factory_3[1] - closest_factory_1[1]
            if distance_delta > 4 : #le 4 est le nombre de tour de production. En 4 tours, un factory 1 produit 4 cyborgs.
                closest_factory = closest_factory_1

    elif len(closest_factory_2) > 0 :

        closest_factory = closest_factory_2

        if len(closest_factory_1) > 0 :
            distance_delta = closest_factory_2[1] - closest_factory_1[1]
            if distance_delta > 3 : #le 3 est le nombre de tour de production. En 3 tours, un factory 1 produit 3 cyborgs.
                closest_factory = closest_factory_1
    
    elif len(closest_factory_1) > 0 :

        closest_factory = closest_factory_1

    elif len(closest_factory_0) > 0 :

        closest_factory = closest_factory_0

    print("closest_factory : ", closest_factory, file=sys.stderr, flush=True) 
    


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
    print("MOVE", str(factory_max_cyborgs), str(closest_factory[0]), str(math.floor(max_cyborgs/3)) )
    #print("WAIT")

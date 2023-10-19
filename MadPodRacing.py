import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

last_round_checkpoint = ()
last_checkpoint = ()
liste_checkpoints = []
start = True
lap = 0
boost = 1
boost_time = ()



def add_checkpoint(next_checkpoint_x, next_checkpoint_y, liste_checkpoints):
    """
    Fonction pour créer une liste des checkpoints de la map.
    """
    checkpoint_en_cours = (next_checkpoint_x, next_checkpoint_y)
    
    if checkpoint_en_cours not in liste_checkpoints :
        liste_checkpoints.append(checkpoint_en_cours)
    
    return liste_checkpoints

def boosting_time(liste_checkpoints):
    """
    Fonction pour calculer la distance entre chaque checkpoint. Et ainsi renvoyer le checkpoint le plus éloigné pour activer le boost
    """
    distance_max = 0
    i = 0
    boosting_time = (-1,-1)

    while i < len(liste_checkpoints) :

        if i+1 == len(liste_checkpoints) :
            distance_between_checkpoints = math.dist(liste_checkpoints[i], liste_checkpoints[0])
        else :
            distance_between_checkpoints = math.dist(liste_checkpoints[i], liste_checkpoints[i+1])

        print("calcul distances : ", distance_between_checkpoints , file=sys.stderr)
        
        
        if distance_between_checkpoints > distance_max :

            distance_max = distance_between_checkpoints
            if i+1 == len(liste_checkpoints):
                boosting_time = liste_checkpoints[0]
            else :
                boosting_time = liste_checkpoints[i+1]
        i +=1

        print("distance max : ", distance_max , file=sys.stderr)

    return boosting_time

def calc_angle_next_turn(x, y, current_checkpoint, next_checkpoint_dist, liste_checkpoints)  :
    """
    Fonction pour calculer l'angle entre le vaisseau et la trajectoire vers le checkpoint après le prochain checkpoint.
    Prenons 3 points :
    A : Position vaisseau
    B : Position checkpoint suivant
    C : Position du checkpoint d'après

    On calcule l'angle du point B
    Donc l'angle formé par la droite entre A et B et la droite entre B et C

    Lorsqu'on est au premier tour, et que les points suivants ne sont pas connus, on calculera l'angle vers le centre de
    la carte (probabilité + élevé de s'approcher de la véritable direction qu'un autre point sur la map)
    """

    #D'abord obtenir les coordonnées du futur checkpoint (position C)



    #Lorsque l'on le connait, on le retrouve dans la liste de nos checkpoints :
    i = 0
    while i < len(liste_checkpoints) :

        if liste_checkpoints[i] == current_checkpoint :

            if i+1 == len(liste_checkpoints) :
                future_checkpoint = liste_checkpoints[0]
            else :
                future_checkpoint = liste_checkpoints[i+1]
        
        i =+ 1

    #Lorsque l'on connait pas le future checkpoint (au premier tour), on considère qu'il est au centre de la map
    if future_checkpoint == current_checkpoint :
        future_checkpoint = (8000,4500)
    
    print("future_checkpoint" ,future_checkpoint, file=sys.stderr)
    print("current_checkpoint" ,current_checkpoint, file=sys.stderr)


    #on calcule les distances que l'on ne connait pas encore :
    distance_between_current_and_future_checkpoints = math.dist(current_checkpoint, future_checkpoint)
    distance_between_ship_and_future_checkpoints = math.dist(current_checkpoint, (x,y) )

    print("distance_between_current_and_future_checkpoints", distance_between_current_and_future_checkpoints , file=sys.stderr)
    print("distance_between_ship_and_future_checkpoints" ,distance_between_ship_and_future_checkpoints, file=sys.stderr)
    print("next_checkpoint_dist" ,next_checkpoint_dist, file=sys.stderr)


    #on calcule l'angle du checkpoint suivant
    a_kwadraat = next_checkpoint_dist**2
    b_kwadraat = distance_between_current_and_future_checkpoints**2
    c_kwadraat = distance_between_ship_and_future_checkpoints**2

    teller = a_kwadraat + b_kwadraat - c_kwadraat
    noemer = 2*next_checkpoint_dist*distance_between_current_and_future_checkpoints
    print("teller" ,teller, file=sys.stderr)
    print("noemer" ,noemer, file=sys.stderr)
    
    result = teller/noemer
    print("result" ,result, file=sys.stderr)

    angle_next_turn = math.acos(teller/noemer)
    #bug à régler, quand je m'approche trop du checkpoint, la précision n'est plus assez bonne et ça foire.
    #AKA désactiver cette fonction quand on est à moins de 600 en distance ? (sur la zone checkpoint quoi)

    return angle_next_turn

    





# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    """Le checkpoint de ce round-ci"""
    current_checkpoint = (next_checkpoint_x, next_checkpoint_y)

    """Après 1 tour, on calcule le meilleur moment pour faire un boost"""

    """
    Mémoriser la dernière instruction de checkpoint, ainsi on peut savoir quand on passe un checkpoint.
    """
    if current_checkpoint != last_round_checkpoint :
        #On sait qu'on vient de passer le checkpoint précédent et on ajoute le suivant à la liste
        turning_point = True
        #add_checkpoint(next_checkpoint_x, next_checkpoint_y, liste_checkpoints)

        print("current_check not the same as last_round" , file=sys.stderr)

        if current_checkpoint not in liste_checkpoints :
            liste_checkpoints.append(current_checkpoint)
        else :
            boost_time = boosting_time(liste_checkpoints)
            print("Boost Time : ", boost_time, file=sys.stderr)



        print("liste_checkpoints : ", liste_checkpoints, file=sys.stderr)
    else :
        turning_point = False
    #reset le checkpoint pour le tour suivant
    last_round_checkpoint = current_checkpoint 

    angle_next_turn = calc_angle_next_turn(x,y,current_checkpoint, next_checkpoint_dist, liste_checkpoints)
    print("angle_next_turn : ", angle_next_turn, file=sys.stderr)

    """------------------------------------------thrust origine----------------------------------------------"""

    print("next_distance : ", next_checkpoint_dist, file=sys.stderr)

    #si le pod est mal aligné, ralentir
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        turning = True
    else :
        turning = False

    if next_checkpoint_dist < 2000 :
        slowing_down = True
    else :
        slowing_down = False

    if turning == True or slowing_down == True :
        thrust = 30
    else :
        thrust = 100

    if boost > 0 :
        #on a qu'un seul boost
        if -5 < next_checkpoint_angle < 5 and current_checkpoint == boost_time :
            boost -= 1
            thrust = "BOOST"
            print("Using BOOOST", current_checkpoint, file=sys.stderr)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " ", str(thrust))

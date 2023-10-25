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

def calc_angle_next_turn(current_checkpoint, next_checkpoint_dist, liste_checkpoints)  :
    """
    Fonction pour calculer l'angle entre le vaisseau et la trajectoire vers le checkpoint après le prochain checkpoint.
    Prenons 3 points :
    A : Position du checkpoint précédent
    B : Position checkpoint suivant (current - direction)
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
                previous_checkpoint = liste_checkpoints[i-1]

            elif i-1 == -1 :
                future_checkpoint = liste_checkpoints[i+1]
                previous_checkpoint = liste_checkpoints[len(liste_checkpoints)-1]

            else :
                future_checkpoint = liste_checkpoints[i+1]
                previous_checkpoint = liste_checkpoints[i-1]                  
        i += 1

    #Lorsque l'on connait pas le future checkpoint (au premier tour), on considère qu'il est au centre de la map
    if lap == 0 : 
        future_checkpoint = (8000,4500)
    
    print("future_checkpoint" ,future_checkpoint, file=sys.stderr)
    print("current_checkpoint" ,current_checkpoint, file=sys.stderr)


    #on calcule les distances que l'on ne connait pas encore :
    distance_between_current_and_future_checkpoints = math.floor(math.dist(current_checkpoint, future_checkpoint))
    distance_between_previous_and_future_checkpoints = math.floor(math.dist(future_checkpoint, previous_checkpoint))

    print("distance_between_current_and_future_checkpoints", distance_between_current_and_future_checkpoints , file=sys.stderr)
    print("distance_between_previous_and_future_checkpoints" ,distance_between_previous_and_future_checkpoints, file=sys.stderr)
    print("next_checkpoint_dist" ,next_checkpoint_dist, file=sys.stderr)

    if distance_between_current_and_future_checkpoints == distance_between_previous_and_future_checkpoints :
        return 0

    #on calcule l'angle du checkpoint suivant
    a_kwadraat = next_checkpoint_dist**2
    b_kwadraat = distance_between_current_and_future_checkpoints**2
    c_kwadraat = distance_between_previous_and_future_checkpoints**2

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
    
def calc_future_checkpoint(current_checkpoint, liste_checkpoints):
    """
    Fonction pour définir le checkpoint après le suivant

    Lorsqu'on est au premier tour, et que les points suivants ne sont pas connus, on utilisera le centre de
    la carte (probabilité + élevé de s'approcher de la véritable direction qu'un autre point sur la map)

    Return le future_checkpoint
    """

    #Premièrement, l'exception lorsque l'on est au LAP 0 et qu'on ne connait pas encore la position des checkpoints :
    if lap == 0 : 
        future_checkpoint = (8000,4500)
    
    else :
    #D'abord obtenir les coordonnées du futur checkpoint (position C)
        i = 0

        print("Calc du futur : current_checkpoint" ,current_checkpoint, file=sys.stderr)

        while i < len(liste_checkpoints) :

            if liste_checkpoints[i] == current_checkpoint :

                if i+1 == len(liste_checkpoints) :
                    future_checkpoint = liste_checkpoints[0]

                else :
                    future_checkpoint = liste_checkpoints[i+1]
        
            i += 1
    
    print("future_checkpoint" ,future_checkpoint, file=sys.stderr)

    return future_checkpoint

def calc_speed(position_last_round, x, y):
    """
    Fonction pour calculer la vitesse du pod.
    Return : Pod Speed en unités/round
    """
    pod_speed = math.floor(math.dist(position_last_round, (x, y)))

    return pod_speed



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

    """
    Mémoriser la dernière instruction de checkpoint, ainsi on peut savoir quand on passe un checkpoint.
    """
    if current_checkpoint != last_round_checkpoint :
        #On sait qu'on vient de passer le checkpoint précédent et on ajoute le suivant à la liste
        #add_checkpoint(next_checkpoint_x, next_checkpoint_y, liste_checkpoints)
        Turning_point = True
        print("current_check not the same as last_round" , file=sys.stderr)

        if current_checkpoint not in liste_checkpoints :
            liste_checkpoints.append(current_checkpoint)

        elif lap == 0 :
            boost_time = boosting_time(liste_checkpoints)
            print("Boost Time : ", boost_time, file=sys.stderr)

        print("liste_checkpoints : ", liste_checkpoints, file=sys.stderr)

    else :
        Turning_point = False

    #reset le checkpoint pour le tour suivant
    last_round_checkpoint = current_checkpoint 

    """
    Compteur de laps
    """
    if len(liste_checkpoints) > 1 :
        if Turning_point == True and current_checkpoint == liste_checkpoints[0]:
            lap += 1
            print("LAP : ", lap, file=sys.stderr)

    """
    Si l'on vient de passer un checkpoint, on modifie la variable du checkpoint futur.
    """
    if Turning_point == True :
        future_checkpoint = calc_future_checkpoint(current_checkpoint, liste_checkpoints)

    """
    #Calcul de l'angle du prochain virage. S'arrête lorsque l'on est au dessus de la zone checkpoint
    if next_checkpoint_dist > 600 :
        angle_next_turn = calc_angle_next_turn(current_checkpoint, next_checkpoint_dist, liste_checkpoints)
        print("angle_next_turn : ", angle_next_turn, file=sys.stderr)
    """

    """----------------------------------Vitesse du pod----------------------------------------------"""

    if start == True :
        #initialiser position last round au premier tour.
        position_last_round = (x, y)
        start = False

    pod_speed = calc_speed(position_last_round, x, y)  
    position_last_round = (x, y)  #enregistrer la position pour le calcul du round suivant

    print("Pod Speed :", pod_speed, file=sys.stderr)

    """----------------------------------puissance de Thrust / Boost----------------------------------------------"""

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
        if -4 < next_checkpoint_angle < 4 and current_checkpoint == boost_time :
            boost -= 1
            thrust = "BOOST"
            print("Using BOOOST", current_checkpoint, file=sys.stderr)

    """
    ---------------------------------------------Direction-------------------------------------------
    """

    #PROCHAINE FOIS --> prendre en compte la distance entre les checkpoints, ralentir en fonction de la distance (ou de
    #la vitesse) plutôt qu'arbitraiement à 2000 du checkpoint.

    #ENSUITE --> voir comment intégrer un décallage dans la direction pour mieux prendre le virage

    direction_modifier = math.floor(next_checkpoint_dist/4)
    
    if slowing_down == True :
        direction_x = future_checkpoint[0]
        direction_y = future_checkpoint[1]
    
    else :
        direction_x = next_checkpoint_x
        direction_y = next_checkpoint_y
        """
        #direction X
        if x < next_checkpoint_x < future_checkpoint[0] :
            direction_x = next_checkpoint_x - direction_modifier
        
        elif x > next_checkpoint_x > future_checkpoint[0] :
            direction_x = next_checkpoint_x + direction_modifier

        else :
            direction_x = next_checkpoint_x

        #direction Y
        if y < next_checkpoint_y < future_checkpoint[1] :
            direction_y = next_checkpoint_y - direction_modifier
        
        elif y > next_checkpoint_y > future_checkpoint[1] :
            direction_y = next_checkpoint_y + direction_modifier

        else :
            direction_y = next_checkpoint_y
        """

    
    print("next_checkpoint : ", current_checkpoint, file=sys.stderr)
    print("next_direction : ", (direction_x, direction_y), file=sys.stderr)
    print("modifier : ", direction_modifier, file=sys.stderr)
    print("slowing down : ", slowing_down, file=sys.stderr)

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(direction_x) + " " + str(direction_y) + " ", str(thrust))

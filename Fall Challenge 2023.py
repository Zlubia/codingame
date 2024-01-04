import sys
import math

# Score points by scanning valuable fish faster than your opponent.

#Variables
fish_type_0 = []
fish_type_1 = []
fish_type_2 = []
fish_type_monster = []

scanned_creatures = []
saved_scans = []

my_drones = []
move_x = 2000
move_y = 10000
light = 0

WEST = 2000
CENTER = 5000
EAST = 8000

TRAVELING_EAST = "Traveling East"
TRAVELING_WEST = "Traveling West"

CEILING_ZONE_0 = 2500
CEILING_ZONE_1 = 5000
CEILING_ZONE_2 = 7500

SURFACE = "surface"
ZONE_0 = "zone 0"
ZONE_1 = "zone 1"
ZONE_2 = "zone 2"

MONSTER = "Monster"
FISH = "Fish"

cleared_zones = {ZONE_0 : False, ZONE_1 : False, ZONE_2 : False}

first_turn = True

#Objects
class Drone:
    def __init__(self, drone_id, drone_x, drone_y, emergency, battery):
        self.drone_id = drone_id
        self.drone_x = drone_x
        self.drone_y = drone_y
        self.emergency = emergency
        self.battery = battery
        self.light = 0
        self.move_x = drone_x
        self.move_y = drone_y
        self.previous_x = drone_x
        self.previous_y = drone_y
        #set Target, can be : MONSTER, FISH, SURFACE, ZONE_0, ZONE_1, ZONE_2
        self.target = ZONE_2
        self.distance_closest_fish = 20000
        if self.drone_x < CENTER :
            self.direction_east_west = TRAVELING_EAST
        else :
            self.direction_east_west = TRAVELING_WEST
    
    def __repr__(self):
        return f"{self.drone_id} {self.drone_x} {self.drone_y} target : {self.target}, direction : {self.move_x},{self.move_y}"


#Functions   
def add_scanned_creatures(creature_id, scanned_list):
    #ajouter les créatures déjà scannées dans la liste.
    if creature_id not in scanned_list:
        scanned_list.append(creature_id)
    
    return scanned_list


def activate_light(my_drones, no_light):
    if no_light == True :
        light = 0
    elif my_drones[i].battery > 5 :
        light = 1
    else :
        light = 0
    
    return light


def search_closest_drone(my_drones, creature_x, creature_y):
    """
    Rerturns ID of closest drone
    """
    closest_distance = 50000
        
    for i in my_drones :
        drone_x = i.drone_x
        drone_y = i.drone_y
        distance_monster = math.dist([creature_x, creature_y], [drone_x, drone_y])
        
        if distance_monster < closest_distance :
            closest_distance = distance_monster
            closest_drone = i.drone_id  
            
    return closest_drone

    
def select_closest_side(drone):
    """
    Returns the closest border of the map
    """
    if drone.drone_x <= CENTER :
        return WEST
    else :
        return EAST


def chose_zone(cleared_zones):
    """Fonction pour définir dans quelle zone aller avec son drone"""

    if cleared_zones[ZONE_0] == False :
        zone_choice = ZONE_0
    elif cleared_zones[ZONE_2] == False :
        zone_choice = ZONE_2
    elif cleared_zones[ZONE_1] == False :
        zone_choice = ZONE_1
    else :
        zone_choice = SURFACE

    return zone_choice

    
def find_depth(drone):
    """
    Returns the Y value for the movement of the drone.
    """
    if drone.target == ZONE_0 :
        drone.move_y = 3250
    elif drone.target == ZONE_1 :
        drone.move_y = 6250
    elif drone.target == ZONE_2 :
        drone.move_y = 9250
    elif drone.target == SURFACE :
        drone.move_y = 0
    else :
        pass
        
    return drone.move_y


def calc_travel_direction_east_west(drone):
    """
    Returns traveling_east or traveling_west. It's the current direction of the drone
    """
    if drone.previous_x < drone.x :
        return TRAVELING_EAST
    elif drone.previous_x > drone.x :
        return TRAVELING_WEST
    else :
        return drone.direction_east_west


#Initial turn
creature_count = int(input())
for i in range(creature_count):
    creature_id, color, _type = [int(j) for j in input().split()]
    if _type == 0 :
        fish_type_0.append(creature_id)
        print("id_type_0",creature_id, file=sys.stderr, flush=True)
    elif _type == 1 :
        fish_type_1.append(creature_id)
        print("id_type_1",creature_id, file=sys.stderr, flush=True)
    elif _type == 2 :
        fish_type_2.append(creature_id)
        print("id_type_2",creature_id, file=sys.stderr, flush=True)
    elif _type == -1 :
        fish_type_monster.append(creature_id)
        print("id_monster",creature_id, file=sys.stderr, flush=True)



# game loop
while True:
    """------VARIABLES A RESET AU DEBUT DU TOUR--------"""
    for i in my_drones :
        i.distance_closest_fish = 20000

    search_zone = -1
    explo_zone_2 = False
    explo_zone_0 = False
    no_light = False
    
    """"------GAME LOOP-------"""
    my_score = int(input())
    foe_score = int(input())

    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input())

        add_scanned_creatures(creature_id, saved_scans)

    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input())


    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]

        if first_turn == True :
            my_drones.append(Drone(drone_id, drone_x, drone_y, emergency, battery))
        else :
            my_drones[i].drone_x = drone_x
            my_drones[i].drone_y = drone_y
            my_drones[i].emergency = emergency
            my_drones[i].battery = battery

        print("Drone ID", drone_id, file=sys.stderr, flush=True)

        print("my drones",my_drones, file=sys.stderr, flush=True)

    foe_drone_count = int(input())
    for i in range(foe_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]

    drone_scan_count = int(input())
    for i in range(drone_scan_count):
        drone_id, creature_id = [int(j) for j in input().split()]

        # Ajouter les fish scannés, uniquement les miens. (Normalement devrait fonctionner avec plusieurs drones)
        for j in my_drones :
            if drone_id == j.drone_id :
                add_scanned_creatures(creature_id, scanned_creatures)
            

    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]

        if creature_id in fish_type_monster :
            #MONSTER
            print("MONSTER ALERT", creature_id, file=sys.stderr, flush=True)

            no_light = True
            
            closest_drone_id = search_closest_drone(my_drones, creature_x, creature_y)

            for j in my_drones :
                if j.drone_id == closest_drone_id :
                    drone_x = j.drone_x
                    drone_y = j.drone_y

            #Find the coordinates of the oposite direction of the monster
            distance_monster = math.dist([creature_x, creature_y], [drone_x, drone_y])

            dx = (creature_x-drone_x)/distance_monster #Normalized vector (direction)
            dy = (creature_y-drone_y)/distance_monster

            move_x = int(drone_x - (distance_monster*dx))
            move_y = int(drone_y - (distance_monster*dy))

            for j in my_drones :
                if j.drone_id == closest_drone_id :
                    j.move_x = move_x
                    j.move_y = move_y
                    j.target = MONSTER
                    print("Running", j, file=sys.stderr, flush=True)
                



            """retiens les coordonnées X, Y du fish le plus proche, pas encore scanné"""
        elif creature_id not in scanned_creatures :
            print("\nSEARCHING_FOR_FISH",my_drones, file=sys.stderr, flush=True)
            print("Creature ID", creature_id, file=sys.stderr, flush=True)

            closest_drone_id = search_closest_drone(my_drones, creature_x, creature_y)

            for j in my_drones :

                if j.target == MONSTER :
                    pass
                elif j.drone_id == closest_drone_id :

                    drone_x = my_drones[j].drone_x
                    drone_y = my_drones[j].drone_y
                    distance_current_fish = math.dist([creature_x, creature_y], [drone_x, drone_y])
                    
                    if distance_current_fish < j.distance_closest_fish :
                        j.distance_closest_fish = distance_current_fish
                        j.move_x = creature_x
                        j.move_y = creature_y
                        j.target = FISH

    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split()
        drone_id = int(inputs[0])
        creature_id = int(inputs[1])
        radar = inputs[2]

    
    """Search_Zone"""
    #SUREMENT REMPLACABLE PAR UNE FONCTION CECI------------------------------------------------------------------------
    if cleared_zones[ZONE_2] == False :
        cleared_zones[ZONE_2] = True
        for j in fish_type_2 :
            if j not in saved_scans :
                cleared_zones[ZONE_2] = False
                break

    if cleared_zones[ZONE_1] == False :
        cleared_zones[ZONE_1] = True
        for j in fish_type_1 :
            if j not in saved_scans :
                cleared_zones[ZONE_1] = False
                break

    if cleared_zones[ZONE_0] == False :
        cleared_zones[ZONE_0] = True
        for j in fish_type_0 :
            if j not in saved_scans :
                cleared_zones[ZONE_0] = False
                break
                

    for i in range(my_drone_count):


        if my_drones[i].target == MONSTER or my_drones[i].target == FISH :
            pass
        else :     
            my_drones[i].target == chose_zone(cleared_zones)

        my_drones[i].move_y = find_depth(my_drones[i])

        if first_turn == True :
            my_drones[i].move_x = select_closest_side(my_drones[i])




        move_x = my_drones[i].move_x
        move_y = my_drones[i].move_y
        light = my_drones[i].light

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        # MOVE <x> <y> <light (1|0)> | WAIT <light (1|0)>
        print(f"MOVE {str(move_x)} {str(move_y)} {str(light)}")

    first_turn = False

import sys
import math

# Score points by scanning valuable fish faster than your opponent.

creature_count = int(input())
for i in range(creature_count):
    creature_id, color, _type = [int(j) for j in input().split()]

#Variables
scanned_creatures = []
my_drones = {}

# game loop
while True:
    """------VARIABLES A RESET AU DEBUT DU TOUR--------"""
    distance_closest_fish = 16000.0
    
    """"------GAME LOOP-------"""
    my_score = int(input())
    foe_score = int(input())

    my_scan_count = int(input())
    for i in range(my_scan_count):
        creature_id = int(input())
        #ajouter les créatures déjà scannées dans la liste.
        if creature_id not in scanned_creatures:
            scanned_creatures.append(creature_id)

    foe_scan_count = int(input())
    for i in range(foe_scan_count):
        creature_id = int(input())


    my_drone_count = int(input())
    for i in range(my_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]
        my_drones[drone_id] = (drone_x, drone_y, emergency, battery)

    foe_drone_count = int(input())
    for i in range(foe_drone_count):
        drone_id, drone_x, drone_y, emergency, battery = [int(j) for j in input().split()]

    drone_scan_count = int(input())
    for i in range(drone_scan_count):
        drone_id, creature_id = [int(j) for j in input().split()]

    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]

        """retiens les coordonnées X, Y du fish le plus proche, pas encore scanné"""
        if creature_id not in scanned_creatures :
            for i in my_drones :
                drone_x = my_drones[i][1]
                drone_y = my_drones[i][2]
                distance_current_fish = math.dist([creature_x, creature_y], [drone_x, drone_y])
                
                if distance_current_fish < distance_closest_fish :
                    distance_closest_fish = distance_current_fish
                    move_x = creature_x
                    move_y = creature_y

    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split()
        drone_id = int(inputs[0])
        creature_id = int(inputs[1])
        radar = inputs[2]
    for i in range(my_drone_count):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        # MOVE <x> <y> <light (1|0)> | WAIT <light (1|0)>
        print(f"MOVE {str(move_x)} {str(move_y)} 0")

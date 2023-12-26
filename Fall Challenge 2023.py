import sys
import math

# Score points by scanning valuable fish faster than your opponent.

#Variables
fish_type_0 = []
fish_type_1 = []
fish_type_2 = []

scanned_creatures = []
saved_scans = []

my_drones = {}
move_x = 2000
move_y = 10000
light = 0

traveling_east = True

ceiling_zone_0 = 2500
ceiling_zone_1 = 5000
ceiling_zone_2 = 7500

zone_0_cleared = False
zone_1_cleared = False
zone_2_cleared = False




#Functions   
def add_scanned_creatures(creature_id, scanned_list):
    #ajouter les créatures déjà scannées dans la liste.
    if creature_id not in scanned_list:
        scanned_list.append(creature_id)
    
    return scanned_list

def activate_light(my_drones):
    if my_drones[i][4] > 5 :
        light = 1
    else :
        light = 0
    
    return light


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



# game loop
while True:
    """------VARIABLES A RESET AU DEBUT DU TOUR--------"""
    distance_closest_fish = 16000.0
    creature_found = False
    search_zone = -1
    
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
        my_drones[i] = (drone_id, drone_x, drone_y, emergency, battery)
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
            if drone_id == my_drones[j][0] :
                add_scanned_creatures(creature_id, scanned_creatures)
            

    visible_creature_count = int(input())
    for i in range(visible_creature_count):
        creature_id, creature_x, creature_y, creature_vx, creature_vy = [int(j) for j in input().split()]

        """retiens les coordonnées X, Y du fish le plus proche, pas encore scanné"""
        if creature_id not in scanned_creatures :
            print("\nSEARCHING_FOR_FISH",my_drones, file=sys.stderr, flush=True)
            
            print("Creature ID", creature_id, file=sys.stderr, flush=True)
            for i in my_drones :
                drone_x = my_drones[i][1]
                drone_y = my_drones[i][2]
                distance_current_fish = math.dist([creature_x, creature_y], [drone_x, drone_y])
                
                if distance_current_fish < distance_closest_fish :
                    distance_closest_fish = distance_current_fish
                    move_x = creature_x
                    move_y = creature_y
                    creature_found = True

    radar_blip_count = int(input())
    for i in range(radar_blip_count):
        inputs = input().split()
        drone_id = int(inputs[0])
        creature_id = int(inputs[1])
        radar = inputs[2]

    
    """Search_Zone"""
    #SUREMENT REMPLACABLE PAR UNE FONCTION CECI------------------------------------------------------------------------
    if zone_2_cleared == False :
        zone_2_cleared = True
        for j in fish_type_2 :
            if j not in saved_scans :
                zone_2_cleared = False

    if zone_1_cleared == False :
        zone_1_cleared = True
        for j in fish_type_1 :
            if j not in saved_scans :
                zone_1_cleared = False

    
    if zone_0_cleared == False :
        zone_0_cleared = True
        for j in fish_type_0 :
            if j not in saved_scans :
                zone_0_cleared = False

    print("zone_0_cleared",zone_0_cleared, file=sys.stderr, flush=True)
                


    for i in range(my_drone_count):

        """Déplacement de la capsule vers la zone voulue"""
        if creature_found == False :

            #direction
            if my_drones[i][1] > 8800 :
                traveling_west = True
            elif my_drones[i][1] < 1200 :
                traveling_east = True

            """----------ZONE 2------------"""
            if zone_2_cleared == False :

                for j in fish_type_2 :
                    print("j",j, file=sys.stderr, flush=True)
                    if j not in scanned_creatures :
                        search_zone = 2
            
                if search_zone == 2 :
                #go to zone and search there

                    if my_drones[i][2] < ceiling_zone_2+1200 :
                        move_x = 1000
                        move_y = 10000
                    else :
                        if traveling_east == True :
                            move_x = 9000
                        elif traveling_west == True :
                            move_x = 1000
                        move_y = 8750

                        light = activate_light(my_drones)
                
                else :
                #get to surface to save the scans
                    move_x = my_drones[i][1]
                    move_y = 0

                    light = activate_light(my_drones)

                """----------ZONE 0------------"""
            elif zone_0_cleared == False :

                for j in fish_type_0 :
                    print("j",j, file=sys.stderr, flush=True)
                    if j not in scanned_creatures :
                        search_zone = 0

                if search_zone == 0 :
                #go to zone and search there

                    if my_drones[i][2] < ceiling_zone_0+1100 or my_drones[i][2] > ceiling_zone_0+1400:
                        move_x = 1000
                        move_y = 3750
                    else :
                        if traveling_east == True :
                            move_x = 9000
                        elif traveling_west == True :
                            move_x = 1000
                        move_y = 3750

                        light = activate_light(my_drones)
                
                else :
                #get to surface to save the scans
                    move_x = my_drones[i][1]
                    move_y = 0

                    light = activate_light(my_drones)

                """----------ZONE 1------------"""
            elif zone_1_cleared == False :

                for j in fish_type_1 :
                    print("j",j, file=sys.stderr, flush=True)
                    if j not in scanned_creatures :
                        search_zone = 1

                if search_zone == 1 :
                #go to zone and search there

                    if my_drones[i][2] < ceiling_zone_1+1100 or my_drones[i][2] > ceiling_zone_1+1400:
                        move_x = 1000
                        move_y = 6250
                    else :
                        if traveling_east == True :
                            move_x = 9000
                        elif traveling_west == True :
                            move_x = 1000
                        move_y = 6250

                        light = activate_light(my_drones)
                
                else :
                #get to surface to save the scans
                    move_x = my_drones[i][1]
                    move_y = 0

                    light = activate_light(my_drones)
            
            
        """RUSTINE - Charger battery si moins de 5"""
        if my_drones[i][4] < 5 :
            light = 0

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        # MOVE <x> <y> <light (1|0)> | WAIT <light (1|0)>
        print(f"MOVE {str(move_x)} {str(move_y)} {str(light)}")

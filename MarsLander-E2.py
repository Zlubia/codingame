import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface_x = [] 
surface_y = []

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface_x.append(land_x)
    surface_y.append(land_y)


#list of coordinates of surface points
print(surface_x, file=sys.stderr, flush=True)
print(surface_y, file=sys.stderr, flush=True)

index = 1

while index < surface_n :

    if surface_y[index] == surface_y[index-1] :
        hauteur_flat = surface_y[index] #hauteur du plateau flat
        debut_flat = surface_x[index-1] #position x de début de flat
        fin_flat = surface_x[index] #position x de fin de flat
        break
    else :
        index += 1


print(" ", file=sys.stderr, flush=True)
print(hauteur_flat, file=sys.stderr, flush=True)
print(debut_flat, file=sys.stderr, flush=True)
print(fin_flat, file=sys.stderr, flush=True)


def move_right(v_speed) :

    if v_speed > -21 :
        rotation = -90
        thrust = 4
    elif -20 > v_speed > -40 :
        rotation = -45
        thrust = 4
    elif v_speed < -39 :
        rotation = -10
        thrust = 4
    
    return (rotation, thrust)

def move_left(v_speed) :

    if v_speed > -21  :
        rotation = 90
        thrust = 4
    elif -20 > v_speed > -40 :
        rotation = 45
        thrust = 4
    elif v_speed < -39 :
        rotation = 10
        thrust = 4
    
    return (rotation, thrust)

def straight_down(v_speed) :

    if v_speed > -21 :
        thrust = 0       
    elif 20 < v_speed < 30 :
        thrust = 2
    elif -20 > v_speed > -40 :
        thrust = 3
    elif v_speed < -39  :
        thrust = 4
    
    rotation = 0

    return (rotation, thrust)

def move_up(v_speed, h_speed) :

    if v_speed > 20 :
        thrust = 0
        rotation = 0   
    elif h_speed > 40 :
        thrust = 4
        rotation = 20
    elif h_speed < -40 :
        thrust = 4
        rotation = -20
    else :
        thrust = 4
        rotation = 0   
   
    return (rotation, thrust)

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    print(v_speed , file=sys.stderr, flush=True)

    #check colision danger
    index = 0
    colision_warning = False

    while index < surface_n :
        
        if x < surface_x[index] and surface_y[index]+500 > y :
            
            colision_warning = True

        index += 1



    #check si on est au dessus de la zone d'atterrisage ou non.

    if x < debut_flat+10 :

        #prendre en compte le risque de colision avec un pic futur
        index = 0
        colision_warning = False

        while index < surface_n :
        
            if x < surface_x[index] and surface_y[index]+500 > y :
            
                colision_warning = True

            index += 1

        if colision_warning == True :
            print("moving up" , file=sys.stderr, flush=True)
            output = move_up(v_speed, h_speed)
        #prendre en compte maintenant la horizontal speed pour ne pas en avoir trop
        elif hauteur_flat + 500 > y :
            print("moving up" , file=sys.stderr, flush=True)
            output = move_up(v_speed)
        elif h_speed < 40 :
            print("moving right" , file=sys.stderr, flush=True)
            output = move_right(v_speed)
        elif h_speed > 40 :
            print("moving left" , file=sys.stderr, flush=True)
            output = move_left(v_speed)
        else :
            print("straight down" , file=sys.stderr, flush=True)
            output = straight_down(v_speed)
    elif x > fin_flat-10 :
        
        #prendre en compte le risque de colision avec un pic futur
        index = 0
        colision_warning = False

        while index < surface_n :
        
            if x > surface_x[index] and surface_y[index]+500 > y :
            
                colision_warning = True

            index += 1

        if colision_warning == True :
            print("moving up" , file=sys.stderr, flush=True)
            output = move_up(v_speed, h_speed)

        #prendre en compte maintenant la horizontal speed pour ne pas en avoir trop
        elif hauteur_flat + 500 > y :
            print("moving up" , file=sys.stderr, flush=True)
            output = move_up(v_speed)
        elif h_speed > -40 :
            print("moving left" , file=sys.stderr, flush=True)
            output = move_left(v_speed)
        elif h_speed < -40 :
            print("moving right" , file=sys.stderr, flush=True)
            output = move_right(v_speed)
        else :
            print("straight down" , file=sys.stderr, flush=True)
            output = straight_down(v_speed)
    else :
        #prendre en compte maintenant la horizontal speed pour la réduire
        
        if y < hauteur_flat + 100 :
            print("straight down" , file=sys.stderr, flush=True)
            output = straight_down(v_speed)
        elif h_speed > 5 :
            print("moving left" , file=sys.stderr, flush=True)
            output = move_left(v_speed)
        elif h_speed < -5 :
            print("moving right" , file=sys.stderr, flush=True)
            output = move_right(v_speed)
        else : 
            print("straight down" , file=sys.stderr, flush=True)
            output = straight_down(v_speed)

    

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(output[0],output[1])

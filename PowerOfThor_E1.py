import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    print("initial_tx: {0}".format(initial_tx), file=sys.stderr)
    print("initial_ty: {0}".format(initial_ty), file=sys.stderr)
    
    print("light_x: {0}".format(light_x), file=sys.stderr)
    print("light_y: {0}".format(light_y), file=sys.stderr)

    if light_x > initial_tx:
        
        direction_x = "E"
        initial_tx += 1
        
    elif light_x == initial_tx:
        
        direction_x = ""
        
    else:
        
        direction_x = "W"
        initial_tx -= 1
        
        
    if light_y > initial_ty:
        
        direction_y = "S"
        initial_ty +=1
        
    elif light_y == initial_ty:
        
        direction_y = ""
        
    else:
        
        direction_y = "N"
        initial_ty -=1
        
    print("direction_x: {0}".format(direction_x), file=sys.stderr)    
    print("direction_y: {0}".format(direction_y), file=sys.stderr) 
    
    direction = direction_y + direction_x
    
    print("direction: {0}".format(direction), file=sys.stderr) 
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)

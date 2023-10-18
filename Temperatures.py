import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
lowest_temp = 10000

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    if abs(t) == abs(lowest_temp) :
        if t < 0 and lowest_temp < 0 :
            lowest_temp = t
        else :
            lowest_temp = abs(t)
    
    elif abs(t) < abs(lowest_temp) :
        lowest_temp = t
        

if n == 0 :
    lowest_temp = 0

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(lowest_temp)

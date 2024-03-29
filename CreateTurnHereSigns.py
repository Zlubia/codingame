import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

_input = input()

print(_input, file=sys.stderr, flush=True)

space = " "
line = ""

instruction = _input.rsplit(" ")

if instruction[0] == "right" :
    character = ">"
elif instruction[0] == "left" :
    character = "<"


howManyArrows = int(instruction[1])
heightOfArrows = int(instruction[2])
strokeThicknessOfArrows = int(instruction[3])
spacingBetweenArrows = int(instruction[4])
additionalIndentOfEachLine = int(instruction[5])

arrow = character*strokeThicknessOfArrows + space*spacingBetweenArrows


for i in range(howManyArrows) :
    line = line + arrow

line = line.rstrip()

print(line, file=sys.stderr, flush=True)

midPoint = int(heightOfArrows/2)

for j in range(midPoint+1) :
    startLine = j*additionalIndentOfEachLine*space
    print(startLine + line)

for k in range(midPoint-1, -1, -1) :
    startLine = k*additionalIndentOfEachLine*space
    print(startLine + line)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

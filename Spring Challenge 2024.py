"""Problem 1"""


def building_heights(n: int, building_map: List[str]) -> List[int]:
    '''

    Args:

        - n (int): The number of buildings
        - building_map (List[str]): Representation of the n buildings

    Returns:

        The height of each building.
    '''

    building_heights = []

    for i in building_map :
        mesure_height = i.count("*")
        building_heights.append(mesure_height)

    return building_heights

"""Problem 2"""

n = int(input())

pixel = "."
pixels = pixel*n
row = list(pixels)
canvas = []

for i in range(n) :
    canvas.append(row)

print(canvas, file=sys.stderr, flush=True)

# game loop
while True:
    command = input()
    print(command, file=sys.stderr, flush=True)
    coord = int(command[2])

    if command.startswith("C") == True :
        for j in canvas :
            j[coord] = "#"
    elif command.startswith("R") == True :
        canvas[coord] = list(pixel*n)

    print(canvas, file=sys.stderr, flush=True)


    for i in canvas:

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # Print the i-th line of the image after the command was executed
        print("".join(i))

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())


def AND_gate (Signal_1,Signal_2) :

    if Signal_1 == '-' and Signal_2 == '-':
        output = '-'
    else :
        output = '_'
    
    return output

def OR_gate (Signal_1,Signal_2) :

    if Signal_1 == '-' or Signal_2 == '-':
        output = '-'
    else :
        output = '_'
    
    return output

def XOR_gate (Signal_1,Signal_2) :

    if Signal_1 == '-' and Signal_2 == '-':
        output = '_'

    elif Signal_1 == '-' or Signal_2 == '-':
        output = "-"

    else :
        output = '_'
    
    return output

def NAND_gate (Signal_1,Signal_2) :

    if Signal_1 == '-' and Signal_2 == '-':
        output = '_'
    else :
        output = '-'
    
    return output

def NOR_gate (Signal_1,Signal_2) :

    if Signal_1 == '_' and Signal_2 == '_':
        output = '-'
    else :
        output = '_'
    
    return output

def NXOR_gate (Signal_1,Signal_2) :

    if Signal_1 == '_' and Signal_2 == '_':
        output = '-'
    elif Signal_1 == '-' and Signal_2 == '-':
        output = '-'
    else :
        output = '_'
    
    return output

    
def Output_Signal (input_A, input_B, Gate):
    
    #Boucle pour sortir la pulse finale - input sont les 2 strings de signals d'input et la fonction Gate à utiliser
    index_max = len(input_A)
    index = 0
    pulse = ""

    while index < index_max :

        pulse = pulse + Gate (input_A[index], input_B[index])
        index += 1

    return pulse


signals_in = {}
output_requests = []

for i in range(n):
    input_name, input_signal = input().split()

    signals_in [input_name] = input_signal

    print(signals_in, file=sys.stderr, flush=True)


for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()

    output_requests.append((output_name, _type, input_name_1, input_name_2))

#print(output_requests, file=sys.stderr, flush=True)



for i in range(m):

    #pour tuple C :
    #input_A = signals_in[output_requests[0][2]]
    #input_B = signals_in[output_requests[0][3]]
    
    #print(output_requests[i][1], file=sys.stderr, flush=True)
    
    if output_requests[i][1] == "AND" :
        Gate_function = AND_gate

    elif output_requests[i][1] == "OR" :
        Gate_function = OR_gate

    elif output_requests[i][1] == "XOR" :
        Gate_function = XOR_gate

    elif output_requests[i][1] == "NAND" :
        Gate_function = NAND_gate

    elif output_requests[i][1] == "NOR" :
        Gate_function = NOR_gate

    elif output_requests[i][1] == "NXOR" :
        Gate_function = NXOR_gate

    pulse = output_requests[i][0] + " " + Output_Signal (signals_in[output_requests[i][2]], signals_in[output_requests[i][3]], Gate_function)


    print(" ", file=sys.stderr, flush=True)



    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(pulse)

from typing import final
import numpy as np

def part_1():
    increased = 0
    
    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]
    
    most_signi = []

    for i in range(len(lines[0])):

        increase_0 = 0
        increase_1 = 0
        
        for x in range(len(lines)):
            if int(lines[x][i]) == 0:
                increase_0 += 1
            elif int(lines[x][i]) == 1:
                increase_1 += 1
        
        if increase_0 < increase_1:
            most_signi.append(1)
        elif increase_0 > increase_1:
            most_signi.append(0)

    # Flip the most signi list
    inv = 1 - np.array(most_signi)
    
    # Convert list to strings so that we can convert from binary later
    most_significant = ''.join(str(n) for n in most_signi)
    inverted = ''.join(map(str, inv))

    # Convert from binary to int
    gamma = int(most_significant, 2)
    epsilon = int(inverted, 2)

    return gamma, epsilon, gamma*epsilon, most_signi

def part_2():
    
    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]

    #co2 = bit_criteria(lines.copy(), "least")
    #oxygen = bit_criteria(lines.copy(), "most")

    oxygen = lines.copy()
    co2 = lines.copy()

    for idx in range(len(lines[0])):   
        if len(oxygen) != 1:
            oxygen = bit_criteria2(oxygen, "oxygen", idx)
        if len(co2) != 1:
            co2 = bit_criteria2(co2, "co2", idx)
    
    #print(oxygen)
    #print(co2)

    print("CO2:    " + co2 + " Int: " + str(int(co2, 2)))
    print("Oxygen: " + oxygen + " Int: " + str(int(oxygen, 2)))

    #return int(co2, 2)*int(oxygen, 2)

def bit_criteria(array, criteria):
    gamma, epsilon, product, signi = part_1()

    for vertical in range(len(signi)):
        for horizontal in array[:]:
            if criteria == "most":
                if int(horizontal[vertical]) != signi[vertical]:
                    array.remove(horizontal)
            if criteria == "least":
                if int(horizontal[vertical]) == signi[vertical]:
                    array.remove(horizontal)
        

    return ''.join(str(n) for n in array)

def bit_criteria2(array, criteria, index=0):
    one_list = []
    zero_list = []
    final_list = []

    for line in array:
        if line[index] == '1':
            one_list.append(line)
        if line[index] == '0':
            zero_list.append(line)


    if criteria == "oxygen":
        #print("oxygen")
        if len(one_list) >= len(zero_list):
            final_list = one_list
        if len(one_list) < len(zero_list):
            final_list = zero_list
    if criteria == "co2":
        #print("co2")
        if len(one_list) >= len(zero_list):
            final_list = zero_list
        if len(one_list) < len(zero_list):
            final_list = one_list

    return final_list



if __name__ == "__main__":
    #print(part_1())
    print(part_2())

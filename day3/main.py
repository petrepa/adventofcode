import numpy as np

def part_1():
    increased = 0
    
    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]
    
    numbers = list(map(int, lines))
    

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

    inv = 1 - np.array(most_signi)
    
    most_significant = ''.join(str(n) for n in most_signi)
    inverted = ''.join(map(str, inv))

    gamma = int(most_significant, 2)
    epsilon = int(inverted, 2)

    return gamma, epsilon, gamma*epsilon

if __name__ == "__main__":
    print(part_1())



def part_1():
    increased = 0
    
    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]
    
    numbers = list(map(int, lines))
    
    for i in range(len(numbers)):

        if numbers[i] > numbers[i-1]:
            increased += 1

    print("Part 1: " + str(increased))

def part_2():
    increased = 0
    
    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]
    
    numbers = list(map(int, lines))
    
    numbers_sum = []

    for i in range(len(numbers)):
        numbers_sum.append(sum(numbers[i:i+3]))
        if numbers_sum[i] > numbers_sum[i-1]:
            increased += 1

    print("Part 2: " + str(increased))

if __name__ == "__main__":
    part_1()
    part_2()
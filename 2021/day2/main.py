

def part_1():
    depth = 0
    postition = 0

    forward = []
    down = []
    up = []

    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]

    for i in range(len(lines)):
        if "forward" in lines[i]:
            forward.append(lines[i][-1])
            forward_int = list(map(int, forward))
        if "down" in lines[i]:
            down.append(lines[i][-1])
            down_int = list(map(int, down))
        if "up" in lines[i]:
            up.append(lines[i][-1])
            up_int = list(map(int, up))

    forward_sum = sum(forward_int)
    down_sum = sum(down_int)
    up_sum = sum(up_int)

    print("Sum of forwards: " + str(forward_sum))
    print("Sum of downs: " + str(down_sum))
    print("Sum of ups: " + str(up_sum))

    depth = down_sum - up_sum

    print("We're at depth: " +str(depth))

    hordep = forward_sum * depth

    return_string = "Final horizontal mulitplied by depth = " + str(hordep)

    return return_string

def part_2():
    depth = 0
    position = 0
    aim = 0

    forward = []
    down = []
    up = []

    with open('list.txt') as f:
        lines = [line.rstrip() for line in f]

    for i in range(len(lines)):
        line = lines[i][-1]

        if "forward" in lines[i]:
            position += int(line)
            depth += aim * int(line)

        if "down" in lines[i]:
            aim += int(line)
        if "up" in lines[i]:
            aim -= int(line)
    
    print("Horizontal position: " + str(position))
    print("Depth: " + str(depth))

    hordep = position * depth
    return_string = "Final horizontal mulitplied by depth = " + str(hordep)

    return return_string

if __name__ == "__main__":
    print(part_1())
    print("-----------------------------")
    print(part_2())
from aocd import get_data

data = get_data(day=4, year=2022)

lines = data.split("\n")


def intersection_of_ranges(a: int, b: int, c: int, d: int):
    x = range(a, b)
    y = range(c, d)
    xs = set(x)

    interseciton = xs.intersection(y)

    if interseciton == set(y) or interseciton == set(x):
        return True
    else:
        return False


def lines_to_pair(lines):
    element_1, _, element_2 = lines.partition(",")
    return string_to_list(element_1), string_to_list(element_2)


def string_to_list(string):
    element_1, _, element_2 = string.partition("-")
    return element_1, element_2


modified_list = []
for line in lines:
    modified_list.append(lines_to_pair(line))


number_of_overlapping_lines = 0

for line in modified_list:
    answer = intersection_of_ranges(
        int(line[0][0]),
        int(line[0][1]),
        int(line[1][0]),
        int(line[1][1]),
    )

    print("Line: " + str(line) + ", Overlap: " + str(answer))

    if answer:
        number_of_overlapping_lines += 1

print(number_of_overlapping_lines)

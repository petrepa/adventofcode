import re

from aocd import get_data

data = get_data(day=4, year=2022)
lines = data.split("\n")

pairs = [
    tuple(map(int, re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()))
    for line in lines
]


print(type(pairs[0]))


def intersection_of_ranges(a: int, b: int, c: int, d: int):
    x = range(a, b)
    y = range(c, d)
    xs = set(x)

    interseciton = xs.intersection(y)

    if interseciton == set(y) or interseciton == set(x):
        return True
    else:
        return False


sum_of_overlaps = sum(1 for i in range(len(pairs)) if intersection_of_ranges(*pairs[i]))

print(sum_of_overlaps)

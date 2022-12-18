import re

from aocd import get_data

data = get_data(day=4, year=2022)
lines = data.split("\n")

pairs = [
    tuple(map(int, re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()))
    for line in lines
]


#      a|---A---|b
#     c|----B----|d

#     a|----A----|b
#      c|---B---|d


def intersection_of_ranges(a: int, b: int, c: int, d: int):
    if a >= c and b <= d:
        return True
    elif a <= c and b >= d:
        return True
    else:
        return False


sum_of_overlaps = sum(1 for i in range(len(pairs)) if intersection_of_ranges(*pairs[i]))

print(sum_of_overlaps)


def overlap_at_all(a: int, b: int, c: int, d: int):
    if a <= c and b >= c:
        return True
    if c <= a and d >= a:
        return True
    else:
        return False


sum_of_overlaps = sum(1 for i in range(len(pairs)) if overlap_at_all(*pairs[i]))
print(sum_of_overlaps)

from aocd import get_data

# remeber to export the AOC_SESSION cookie
# OPONENT
# A = rock
# B = paper
# C = scissor

# YOU
# X = rock
# Y = paper
# Z = scissor

guide = get_data(day=2, year=2022)
guide_line = guide.split("\n")

# inspired by @trulshj (https://github.com/trulshj/AdventOfCode/blob/main/2022/python/day02.py)
strategy_guide = {
    "A": {"X": 1 + 3, "Y": 2 + 6, "Z": 3 + 0},
    "B": {"X": 1 + 0, "Y": 2 + 3, "Z": 3 + 6},
    "C": {"X": 1 + 6, "Y": 2 + 0, "Z": 3 + 3},
}


score_sum = sum(
    [strategy_guide[line[0]][line[2]] for line in guide_line if line.strip()]
)

print(score_sum)

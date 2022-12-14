import numpy as np

# open the file with all of the calories
f = open("elf_calories.txt", "r")

# somewhere to store the total calories of an elf
total_calories_for_a_elf = []
# a place to count all the calories of the elf before we put it in the store
elf_calories = 0

for line in f:
    # if the line is a number add it to the counter
    if line.strip():
        elf_calories = elf_calories + int(line)
    # if the line is not a number but a line shift, add the counter entry to the total and reset the counter
    if line.strip() == "":
        total_calories_for_a_elf.append(elf_calories)
        elf_calories = 0

print(
    "The elf carrying the most calories, is carrying {0} calories".format(
        max(total_calories_for_a_elf)
    )
)


def top_in_list(N: int, search_list: list):
    a = np.array(search_list)
    index = np.argpartition(a, -N)[-N:]

    return a[index]


def print_top_elves(top_list):
    for index, item in enumerate(top_list):
        print("              Elf {0}: {1} calories".format(index, item))


def total_of_top_list(top_list):
    return sum(top_list)


print("Top 3 elves:")
top_list = top_in_list(3, total_calories_for_a_elf)

print_top_elves(top_list)

print("Sum of top 3 elves: {0} calories".format(total_of_top_list(top_list)))

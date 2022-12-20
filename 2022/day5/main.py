from re import match

from aocd import get_data

data = get_data(day=5, year=2022)

new_data = data.split("\n\n")


#     [C]             [L]         [T]
#     [V] [R] [M]     [T]         [B]
#     [F] [G] [H] [Q] [Q]         [H]
#     [W] [L] [P] [V] [M] [V]     [F]
#     [P] [C] [W] [S] [Z] [B] [S] [P]
# [G] [R] [M] [B] [F] [J] [S] [Z] [D]
# [J] [L] [P] [F] [C] [H] [F] [J] [C]
# [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
#  1   2   3   4   5   6   7   8   9


puzzle = new_data[0].split("\n")
instructions = new_data[1]

indexes = puzzle[-1].replace(" ", "")
stacks = {int(index): [] for index in indexes}


for line in puzzle[:-1]:
    for index, crate in enumerate(line[1::4], start=1):
        if crate != " ":
            stacks[index].insert(0, crate)

instruct = []
for instruction in instructions.split("\n"):
    instruct.append(match(r"move (\d+) from (\d+) to (\d+)", instruction).groups())


for times, from_stack, to_stack in instruct:
    number_of_items_from_stack = len(stacks[int(from_stack)]) - int(times)
    print("Time: " + str(times) + " From: " + str(from_stack) + " To: " + str(to_stack))
    # print(stacks[int(from_stack)])

    stacks[int(to_stack)].extend(stacks[int(from_stack)][-int(times) :][::1])

    del stacks[int(from_stack)][-int(times) :]


for stack in stacks:
    try:
        print(stacks[stack][-1])
    except:
        pass

print(stacks[6])
print(stacks[7])
print("Moving")
stacks[7].extend(stacks[6][-5:][::1])
print(stacks[7])
print("Deleting")
del stacks[6][-5:]
print(stacks[6])

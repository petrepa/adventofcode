from aocd import get_data

data = get_data(day=3, year=2022)


def find_similarity(string_a, string_b):
    for ia, ca in enumerate(string_a):
        for ib, cb in enumerate(string_b):
            if ca == cb:
                return ca


rucksacks = data.split("\n")

type_in_both_compartments = []

for rucksack in rucksacks:
    number_of_items = len(rucksack)
    compartment_1 = rucksack[: number_of_items // 2]
    compartment_2 = rucksack[number_of_items // 2 :]

    type_in_both_compartments.append(find_similarity(compartment_1, compartment_2))

priorities = {}
for i, letter in enumerate(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1
):
    priorities[letter] = i


sum_of_priorities = sum(
    [priorities[item_type] for item_type in type_in_both_compartments]
)

print("Part 1: " + str(sum_of_priorities))


def find_similarity_2(string_a, string_b, string_c):
    for ia, ca in enumerate(string_a):
        for ib, cb in enumerate(string_b):
            for ic, cc in enumerate(string_c):
                if ca == cb == cc:
                    return ca


new_list = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

badge_types = []
for items in new_list:
    badge_types.append(find_similarity_2(items[0], items[1], items[2]))

sum_of_badge_priorities = sum(priorities[item_type] for item_type in badge_types)

print("Part 2: " + str(sum_of_badge_priorities))

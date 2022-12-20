from aocd import get_data

data = get_data(day=6, year=2022)

four_character = data[0:4]


def find_character_index(distinct_characters: int):
    for i in range(0, len(data)):
        four = []
        four_characters = data[i : i + distinct_characters]
        for character in four_characters:
            four.append(four_characters.count(character))
        if four.count(1) == distinct_characters:
            return i + distinct_characters


print("Part 1: " + str(find_character_index(4)))
print("Part 2: " + str(find_character_index(14)))

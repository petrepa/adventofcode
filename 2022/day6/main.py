from aocd import get_data

data = get_data(day=6, year=2022)

four_character = data[0:4]


def find_character_index():
    for i in range(0, len(data)):
        four = []
        four_characters = data[i : i + 4]
        for character in four_characters:
            four.append(four_characters.count(character))
        if four.count(1) == 4:
            return i + 4


print(find_character_index())

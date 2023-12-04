from aocd import get_data
import re

data = get_data(day=2, year=2023)


def first_task():
    red = 12
    green = 13
    blue = 14

    red_count = 0
    green_count = 0
    blue_count = 0

    game_id_sum = 0
    
    for game in data.splitlines():
        game_id = re.findall("Game (\d+)", game)[0]
        game = game.split(":")[1]
        rounds = game.split(';')

        red_count = 0
        green_count = 0
        blue_count = 0

        for round in rounds:
            values = re.findall(r"(\d+) (red|green|blue)", round)

            for value in values:
                if value[1] == "red":
                    red_count += int(value[0])
                elif value[1] == "green":
                    green_count += int(value[0])
                elif value[1] == "blue":
                    blue_count += int(value[0])
        # print(rounds)

        if red_count <= red and green_count <= green and blue_count <= blue:
            print(f"Game ID: {game_id} - Red count: {red_count}, Green count: {green_count}, Blue count: {blue_count}")
            print(f"Innafor - {game_id_sum} + {game_id} = {game_id_sum + int(game_id)}")
            game_id_sum += int(game_id)
        print("\n\n")
    print(f"Game ID-sum: {game_id_sum}")

# first_task()

def first_task2():
    red = 12
    green = 13
    blue = 14

    red_count = 0
    green_count = 0
    blue_count = 0

    game_id_sum = 0
    
    for game in data.splitlines():
        game_id = re.findall("Game (\d+)", game)[0]
        game = game.split(":")[1]
        rounds = game.split(';')

        red_count = 0
        green_count = 0
        blue_count = 0

        for round in rounds:
            values = re.findall(r"(\d+) (red|green|blue)", round)
            for value in values:
                round_good = False
                if value[1] == "red" and int(value[0]) > red:
                    break
                elif value[1] == "green" and int(value[0]) > green:
                    break
                elif value[1] == "blue" and int(value[0]) > blue:
                    break
                else:
                    round_good = True
            if round_good == False:break
            game_id_sum += int(game_id)
    print(game_id_sum)


first_task2()
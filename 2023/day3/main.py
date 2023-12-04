from aocd import get_data
import re

data = get_data(day=3, year=2023)
lines = data.splitlines()

def data_to_array(data):
    return [list(line) for line in lines]


array = data_to_array(data)

symbols_pattern = r"[^.\d]"
numbers_pattern = r"\d+"

for row in range(len(array)):
    # for col in range(len(array[row])):
    number_matches = re.finditer(numbers_pattern, lines[row])
    for match in number_matches:
        # print(lines[row], match.start(), match.end())
        # print(match.group(0), match.start(), match.end())
        if match.end() > 139:
            # print(range(match.start(), match.end()))
            for col in range(match.start(), match.end()):
                print(f"Col: {col}")
                if 0 <= row < len(array) and 0 <= col < len(array[0]):
                    print("")
                else: 
                    print("False")
                    symbol_match_to_right = re.findall(symbols_pattern, array[row][col+1])
                # if 0 <= row < len(array) and 0 <= col < len(array[0]):
                #     print(len(array[0]))
                #     print(f"Col: {col+1}")
                #     symbol_match_to_left = re.findall(symbols_pattern, array[row][col-1])
                #     symbol_match_to_right = re.findall(symbols_pattern, array[row][col+1])
            #         symbol_match_to_above = re.findall(symbols_pattern, array[row-1][col])
            #         symbol_match_to_under = re.findall(symbols_pattern, array[row+1][col])
            #         symbol_match_to_above_left = re.findall(symbols_pattern, array[row-1][col-1])
            #         symbol_match_to_above_right = re.findall(symbols_pattern, array[row-1][col+1])
            #         symbol_match_to_under_left = re.findall(symbols_pattern, array[row+1][col-1])
            #         symbol_match_to_under_right = re.findall(symbols_pattern, array[row+1][col+1])
            #     if symbol_match_to_left or symbol_match_to_right or symbol_match_to_above or symbol_match_to_under or symbol_match_to_above_left or symbol_match_to_above_right or symbol_match_to_under_left or symbol_match_to_under_right:
            #         print("maatch")
            #         # print(number_match.group(0), row, col)

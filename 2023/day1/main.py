from aocd import get_data
import re

data = get_data(day=1, year=2023)

def first_task():
    sum_calibration_values = 0

    # print(re.search(r'\d+', data.splitlines()[3]).group()[0])
    # print(re.search(r'\d+', data.splitlines()[3]).group()[-1])
    for line in data.splitlines():
        print(line)
        numbers = ''.join(re.findall(r'\d+', line))
        print(numbers)
        first_digit = numbers[0]
        last_digit = numbers[-1]
        calibration_value = int(first_digit)*10+int(last_digit)
        print(f"Calibration value: ", calibration_value)
        sum_calibration_values += int(calibration_value)
        print(f"Sum of calib: ", sum_calibration_values)
        print("\n\n")

    print(f"Sum of all calibraiton values: ", sum_calibration_values)


# first_task() # Your puzzle answer was 54697.

def second_task():
    word_to_number = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    numbers_in_words = list(word_to_number.keys())
    print(numbers_in_words)


    sum_calibration_values = 0

    for line in data.splitlines():
        print(line)
        numbers = re.findall(r'(\d|' + '|'.join(numbers_in_words) + ')', line)
        print(f"numbers: ", numbers)
        converted_list = []
        for number in numbers:
            if number in word_to_number:
                converted_list.append(word_to_number[number])
            else:
                converted_list.append(int(number))
        print(converted_list)
        first_digit = converted_list[0]
        print(f"first digit: ", first_digit)
        last_digit = converted_list[-1]
        print(f"last digit: ", last_digit)
        calibration_value = int(first_digit)*10+int(last_digit)
        print(f"Calibration value: ", calibration_value)
        sum_calibration_values += int(calibration_value)
        print(f"Sum of calib: ", sum_calibration_values)
        print("\n\n")

    print(f"Sum of all calibraiton values: ", sum_calibration_values)

second_task()

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

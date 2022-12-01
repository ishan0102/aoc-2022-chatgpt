# Open the input file and read in the input as a string
with open('inputs/day-1.txt') as f:
  input_str = f.read()

# Split the input string by newline characters to create a list of strings
input_lines = input_str.strip().split('\n\n')

# Split each string by newline characters to create a list of lists of strings
calorie_lists = [line.split('\n') for line in input_lines]

# Convert each string to an integer and add the integers in each list together
# to find the total number of Calories for each Elf
calorie_totals = [sum(map(int, cal_list)) for cal_list in calorie_lists]

# Sort the list of total Calories in descending order and print the sum of the first three numbers
print(sum(sorted(calorie_totals, reverse=True)[:3]))
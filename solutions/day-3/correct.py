import string

with open ('inputs/day-3.txt', 'r') as f:
    rucksacks = f.read().splitlines()

# Create a mapping from lowercase characters to their priorities
lowercase_priorities = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
# Create a mapping from uppercase characters to their priorities
uppercase_priorities = {c: i + 27 for i, c in enumerate(string.ascii_uppercase)}

# The sum of the priorities of the item types that appear in both compartments
# of each rucksack
total_priority = 0

for rucksack in rucksacks:
    # Split the rucksack into two parts
    first_compartment = rucksack[: len(rucksack) // 2]
    second_compartment = rucksack[len(rucksack) // 2 :]

    # Create sets containing the characters in each compartment
    first_set = set(first_compartment)
    second_set = set(second_compartment)

    # Find the characters that appear in both compartments
    common_chars = first_set.intersection(second_set)

    for char in common_chars:
        # Add the priority of the character to the total
        if char in lowercase_priorities:
            total_priority += lowercase_priorities[char]
        elif char in uppercase_priorities:
            total_priority += uppercase_priorities[char]

# Print the total priority
print(total_priority)

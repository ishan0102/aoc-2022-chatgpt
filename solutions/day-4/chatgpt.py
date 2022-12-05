# Read the input
pairs = []
for line in open("../../inputs/day-4.txt"):
  # Parse the range for each pair
  a, b = map(int, line.strip().split("-"))
  pairs.append((a, b))

# Count the number of pairs where one range fully contains the other
count = 0
for i in range(len(pairs)):
  # Get the ranges for the current pair
  a1, a2 = pairs[i]

  # Check if the other range in the same row fully contains the current range
  b1, b2 = pairs[1-i]
  if (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2):
    count += 1

# Print the result
print(count)

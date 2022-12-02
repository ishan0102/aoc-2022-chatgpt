# Open the input file and read the strategy guide
with open('inputs/day-2.txt') as f:
  strategy_guide = f.read()

# Initialize the total score to 0
total_score = 0

# Create a dictionary that maps each letter to its corresponding score
letter_scores = {"X": 1, "Y": 2, "Z": 3}
shape_map = {"A": "X", "B": "Y", "C": "Z"}

# Split the strategy guide into a list of rounds, where each round is represented as a string of length 5
rounds = []
for i in range(0, len(strategy_guide), 4):
  rounds.append(strategy_guide[i:i+4])

# Loop through each round in the strategy guide
for round in rounds:
  # Get the opponent's hand shape and your hand shape for this round
  opponent_shape = round[0]
  my_shape = round[2]

  # Initialize the round score to the score of your hand shape
  round_score = letter_scores[my_shape]

  # If the round is a draw, add 3 to the round score
  if shape_map[opponent_shape] == my_shape:
    round_score += 3

  # If you won the round, add 6 to the round score
  elif (opponent_shape == "A" and my_shape == "Y") or (opponent_shape == "B" and my_shape == "Z") or (opponent_shape == "C" and my_shape == "X"):
    round_score += 6

  # Add the round score to the total score
  total_score += round_score

# Print the total score
print(total_score)

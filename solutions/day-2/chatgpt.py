# Open the input file and read the strategy guide
with open('inputs/day-2.txt') as input_file:
  strategy_guide = input_file.read()

# Initialize the total score to 0
total_score = 0

# Create a dictionary that maps each letter to its corresponding score
letter_scores = {"A": 1, "B": 2, "C": 3}

# Split the strategy guide into a list of rounds, where each round is represented as a string of length 5
rounds = [strategy_guide[i:i+5] for i in range(0, len(strategy_guide), 5)]

# Loop through each round in the strategy guide
for round in rounds:
  # Get the opponent's hand shape and your hand shape for this round
  opponent_shape = round[0]
  my_shape = round[4]

  # Initialize the round score to the score of your hand shape
  round_score = letter_scores[my_shape]

  # If the round is a draw, add 3 to the round score
  if opponent_shape == my_shape:
    round_score += 3

  # If you won the round, add 6 to the round score
  elif (opponent_shape == "A" and my_shape == "Z") or (opponent_shape == "B" and my_shape == "X") or (opponent_shape == "C" and my_shape == "Y"):
    round_score += 6

  # Add the round score to the total score
  total_score += round_score

# Print the total score
print(total_score)

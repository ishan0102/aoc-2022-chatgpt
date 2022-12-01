# Advent-of-Code 2022: ChatGPT Edition
OpenAI's ChatGPT model came out today (November 30), one day before the start of the Advent-of-Code 2022. I thought it would be interesting to let ChatGPT solve each day's puzzle and see how close it gets to the correct solution. Each day, I'll use ChatGPT as a starting point and modify the solution minimally until it works. I think this is a pretty interesting task for a few reasons:
- Advent-of-Code puzzles are generally unique and worded with lots of natural language, so it's unlikely that the model has seen similar inputs before.
- Advent-of-Code is a decent proxy for measuring basic programming skills.
- The multiple parts to each puzzle make it a good test of the model's ability to generalize to updated instructions and retain context.

## Prompting ChatGPT
Each day, I'll simply copy the prompt from the puzzle as-is and append one sentence to the end: "Take input from a file located at inputs/day-1.txt." This should force ChatGPT to read the input from a file instead of `input()` which is what it does without prompting. I suspect there may be file path issues in the future, but I'll fix errors related to that without penalizing ChatGPT since I think it's a reasonable assumption that the model would be able to read from a file.

## Usage
You can run `main.py` and input the day to run ChatGPT's solutions and the correct solutions. You'll see something like this:

<img width="400" alt="image" src="https://user-images.githubusercontent.com/47067154/204980550-ad03b3e3-258b-4f4a-bbc1-a997bad9f69e.png">


## Recap
| Day | Puzzle | Errors |
| --- | --- | --- |
| 1 | [Calorie Counting](https://adventofcode.com/2022/day/1) | Split newlines incorrectly in the input file. |

## Details

### Day 1: Calorie Counting
The first error I ran into was a `ValueError: invalid literal for int() with base 10: ''`. I realized the model was splitting the newlines incorrectly causing it to read an empty string as a number, which was easily fixed by having it split input on `\n\n` instead of `\n`.

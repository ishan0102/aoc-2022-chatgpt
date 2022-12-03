# Advent-of-Code 2022: ChatGPT Edition
OpenAI's ChatGPT model came out today (November 30), one day before the start of the Advent-of-Code 2022. I thought it would be interesting to let ChatGPT solve each day's puzzle and see how close it gets to the correct solution. Each day, I'll use ChatGPT as a starting point and modify the solution minimally until it works. I think this is a pretty interesting task for a few reasons:
- Advent-of-Code puzzles are generally unique and worded with lots of natural language, so it's unlikely that the model has seen similar inputs before.
- Advent-of-Code is a decent proxy for measuring basic programming skills.
- The multiple parts to each puzzle make it a good test of the model's ability to generalize to updated instructions and retain context.
I'll only do part 1 of each puzzle to make things easier, especially because a lot of the same errors appear in both parts which makes it less interesting.

## Prompting ChatGPT
Each day, I'll copy the prompt from the puzzle as-is and see what happens. Based on day 1 and 2, the prompts generally work well but I've had to make a few modifications like telling it to read from a file or specifying what the input specifications are. I'm trying to give ChatGPT the best odds of solving the problem correctly to determine the model's capabilities at the algorithmic portion of the problem and not other tedious tasks.

## Usage
You can run `main.py` and input the day to run ChatGPT's solutions and the correct solutions. You'll see something like this:

<img width="400" alt="image" src="https://user-images.githubusercontent.com/47067154/204980550-ad03b3e3-258b-4f4a-bbc1-a997bad9f69e.png">

Each day's puzzles are located in `solutions/day-XX` and `chatgpt.py` is ChatGPT's solution while `correct.py` is the corrected version. You can find the corresponding input files in `inputs/day-XX`.

## Recap
| Day | Puzzle | Errors |
| --- | --- | --- |
| 1 | [Calorie Counting](https://adventofcode.com/2022/day/1) | Split newlines incorrectly in the input file. |
| 2 | [Rock Paper Scissors](https://adventofcode.com/2022/day/2) | Read input file incorrectly. Off-by-one error. Used variable names that didn't associate with the prompt. |
| 3 | [Rucksack Reorganization](https://adventofcode.com/2022/day/3) | Worked perfectly. |

## Details

### Day 1: Calorie Counting
The first error I ran into was a `ValueError: invalid literal for int() with base 10: ''`. I realized the model was splitting the newlines incorrectly causing it to read an empty string as a number, which was easily fixed by having it split input on `\n\n` instead of `\n`.

### Day 2: Rock Paper Scissors
Right off the bat, ChatGPT seems to get confused on how the strategy guide works so I had to prompt it a bit to explain that the dictionary keys should be `A`, `B`, and `C` instead of `Rock`, `Paper`, and `Scissors`. After that, I hit a `KeyError: ' '` which is because of how it was reading in the input. Then, there were a few minor errors like an off-by-one for the number of characters to read in per line (5 instead of 4) which resulted in an `IndexError`. Also, ChatGPT forgot that `A` associates with `X` and so on, so I had to add an extra map for that. After that, it worked perfectly.

### Day 3: Rucksack Reorganization
Not sure what to say here because it just worked perfectly on the first try. No notes!

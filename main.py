# Driver to run Advent-of-Code for ChatGPT and the correct solutions
def run_code(filepath):
    with open(filepath, "r") as f:
        code = f.read()
    
    try:
        exec(code)
    except Exception as e:
        print("Error: ", e)

def get_solutions(day):
    print(f"Running solution for day {day} on ChatGPT...")
    run_code(f"solutions/day-{day}/part1-chat.py")
    print(f"\nRunning modified solution for day {day}...")
    run_code(f"solutions/day-{day}/part1-me.py")
    print(f"\nRunning solution for day {day} on ChatGPT...")
    run_code(f"solutions/day-{day}/part2-chat.py")
    print(f"\nRunning modified solution for day {day}...")
    run_code(f"solutions/day-{day}/part2-me.py")

def main():
    day = input("Which day do you want to run? ")
    if int(day) < 1 or int(day) > 1:
        print("Invalid day.")
        return

    # print a pretty ascii banner that says advent of code - chatgpt edition
    print("""
 __| |____________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
   | |                                            | |
   | |      Advent of Code – ChatGPT Edition      | |
   | |                                            | |
   | |                                            | |
 __| |____________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |

    """)
    get_solutions(day)

if __name__ == "__main__":
    main()

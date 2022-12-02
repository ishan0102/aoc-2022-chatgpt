# Driver to run Advent-of-Code for ChatGPT and the correct solutions
from datetime import datetime, timezone, timedelta

def run_code(filepath):
    with open(filepath, "r") as f:
        code = f.read()
    
    try:
        exec(code)
    except Exception as e:
        print("Error: ", e)

def get_solutions(day):
    print(f"Day {day} Solutions:")
    print("=============")
    print(f"Running ChatGPT...")
    run_code(f"solutions/day-{day}/chatgpt.py")
    print(f"\nRunning correct solution...")
    run_code(f"solutions/day-{day}/correct.py")
    print("\n")

def days_since_dec1():
    # Create a datetime object for December 1, 2022, 12am ET
    target_datetime = datetime(2022, 12, 1, 0, 0, 0, tzinfo=timezone(-timedelta(hours=5)))
    current_datetime = datetime.now(timezone(-timedelta(hours=5)))
    difference = current_datetime - target_datetime
    return difference.days

def main():
    day = input("\nWhich day do you want to run? ")
    current_day = days_since_dec1() + 1
    if day == '' or int(day) < 1 or int(day) > current_day:
        print(f"Invalid day. Must be between 1 and {current_day}.\n")
        return

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

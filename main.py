# Driver to run Advent-of-Code for ChatGPT and the correct solutions
from datetime import datetime, timezone, timedelta

def run_code(filepath):
    with open(filepath, "r") as f:
        code = f.read()

    try:
        exec(code)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

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

    current_day = days_since_dec1() + 1
    day = input(f"\nWhich day do you want to run? Can be a number from 1 to {current_day} or 'all': ")
    print("\n")

    if day == "all":
        for i in range(1, current_day + 1):
            get_solutions(i)

    elif day != '' and int(day) >= 1 and int(day) <= current_day:
        get_solutions(day)
        
    else:
        print(f"Invalid day. Must be between 1 and {current_day}.\n")


if __name__ == "__main__":
    main()

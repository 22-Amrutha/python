print("name:amrutha;usn:1AY24AI007;SECTION:M")

from datetime import datetime, timedelta

def print_current_day():
    today = datetime.today()
    print("\n1. Current Day of the Week:")
    print("Today is:", today.strftime("%A"))

def birthday_info():
    print("\n2. Birthday Info:")
    birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
    today = datetime.today()

    # Calculate age
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    # Calculate next birthday
    next_birthday = birthday.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    time_remaining = next_birthday - today
    days = time_remaining.days
    hours = time_remaining.seconds // 3600
    minutes = (time_remaining.seconds % 3600) // 60
    seconds = time_remaining.seconds % 60

    print(f"You are {age} years old.")
    print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

def double_day(birth1, birth2):
    if birth1 > birth2:
        birth1, birth2 = birth2, birth1
    diff = birth2 - birth1
    return birth2 + diff

def n_times_day(birth1, birth2, n):
    if birth1 > birth2:
        birth1, birth2 = birth2, birth1
        n = 1 / n
    diff = birth2 - birth1
    return birth2 + diff / (n - 1)

def run_double_day():
    print("\n3. Double Day:")
    b1_str = input("Enter first birthday (YYYY-MM-DD): ")
    b2_str = input("Enter second birthday (YYYY-MM-DD): ")
    b1 = datetime.strptime(b1_str, "%Y-%m-%d")
    b2 = datetime.strptime(b2_str, "%Y-%m-%d")

    result = double_day(b1, b2)
    print("Double Day is on:", result.strftime("%Y-%m-%d"))

def run_n_times_day():
    print("\n4. N-Times Day:")
    b1_str = input("Enter first birthday (YYYY-MM-DD): ")
    b2_str = input("Enter second birthday (YYYY-MM-DD): ")
    n = float(input("Enter the age ratio (e.g., 2 for twice as old): "))

    b1 = datetime.strptime(b1_str, "%Y-%m-%d")
    b2 = datetime.strptime(b2_str, "%Y-%m-%d")

    result = n_times_day(b1, b2, n)
    print(f"The day when one is {n} times older than the other is: {result.strftime('%Y-%m-%d')}")

# Main Execution
if __name__ == "__main__":
    print_current_day()
    birthday_info()
    run_double_day()
    run_n_times_day()

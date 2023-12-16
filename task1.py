from datetime import datetime, timedelta, date
from collections import defaultdict


def get_birthdays_per_week(users):
    # Data Preparation
    birthday_dict = defaultdict(list)

    # Getting the current date
    today = datetime.now().date()

    # Iterating through users
    for user in users:
        # Converting the birthday date
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Evaluating the birthday for this year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Comparing with the current date
        delta_days = (birthday_this_year - today).days

        # Determining the day of the week
        if delta_days < 7:
            birthday_date = today + timedelta(days=delta_days)
            if birthday_date.weekday() >= 5:  # 5 is Saturday, 6 is Sunday
                # If the birthday is on a weekend, greet on Monday
                day_of_week = "Monday"
            else:
                day_of_week = birthday_date.strftime("%A")

            # Storing the result
            birthday_dict[day_of_week].append(name)

    # Printing the result
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")


# Example users list with birthdays
users = [
    {"name": "Andrii Lozinskyi", "birthday": datetime(1990, 12, 16)},
    {"name": "Artem Denysov", "birthday": datetime(1990, 12, 18)},
    {"name": "Artur Mykhailiuk", "birthday": datetime(1990, 12, 19)},
    {"name": "Katherine Zhdanova", "birthday": datetime(1940, 12, 22)},
    {"name": "Hanna Komrakova", "birthday": datetime(1939, 12, 24)},
]

# Call the function with the users list to get birthdays for the next week
get_birthdays_per_week(users)

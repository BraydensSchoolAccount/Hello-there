# Hello there Customer
# Brayden Towner
# 11/28/2023

import os

os.system("cls")

DAYS_OF_WEEK = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def get_input():
    """Get the inputs from the user, can rerun
        Return: age(int, The age of the user), day_of_week(int, The numerical day of the week)
    """
    age = int(input("What is the age of the person going? >  "))
    day_of_week = int(input("What is the day of the week? (1 = Sunday to 7 = Saturday) >  "))
    # Confirmation Message
    print(
        f'''Age: {age}
Day of the week: {DAYS_OF_WEEK[day_of_week-1].title()}
Is this correct?
'''
    )
    # Ask user to day yes or no. It only checks for yes
    user_confirm = input("Y/Yes or N/No >  ").lower()
    # If the answer isn't explicitly y or yes, go again
    if not (user_confirm == "y" or user_confirm == "yes"):
        os.system("cls")
        get_input()
    return age, day_of_week

def calculate_price(upcharge):
    sum = 0
    if age <= 12:
        sum = 4
    elif age <= 18:
        sum = 5
    elif age <= 60:
        sum = 6
    else:
        sum = 3
    sum += upcharge
    print(f"The price is ${sum:.2f}!")


print("Welcome to the game dev burning!")
# This does work
age, day_of_week = get_input()
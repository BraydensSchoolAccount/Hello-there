# Hello there Customer
# Brayden Towner
# 11/28/2023

# To clarify, these comments are for the teacher
# We have learned While and Try/Except
# I may know of constants, but I would only capitalize it to remind myself it shouldn't be changed, even if I didn't

import os

os.system("cls")

# Listed days
DAYS_OF_WEEK = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def get_input():
    """Get the inputs from the user, can rerun
        Return: age(int, The age of the user), day_of_week(int, The numerical day of the week)
    """
    # Set the value of age below 0 so while loop runs, same with day_of_week. This is to prevent redundant code
    age, day_of_week = -1, -1
    # Checking if age is invalid
    while age < 0:
        age = int(input("What is the age of the person going? >  "))
        # Print only if age is invalid
        if age < 0:
            os.system("cls")
            print("Please enter valid age")
    # The day doesn't matter if they are 6 and under, included for user convenience
    if age <=6:
        return age, 0
    os.system("cls")
    # If it's not a valid index, keep running
    while not 0 <= day_of_week <= 6:
        # Prevents errors
        try:
            day_of_week = DAYS_OF_WEEK.index(input("What is the day of the week? >  ").strip().lower())
        except:
            os.system("cls")
            print("Please enter valid day (sunday - saturday)")
    os.system("cls")
    # Confirmation Message
    print(
        f'''Age: {age}
Day of the week: {DAYS_OF_WEEK[day_of_week].title()}
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

def calculate_price(age, upcharge):
    """Calculates the price based on the age of the person and an upcharge

    Args:
        upcharge (float): The upcharge of the ticket
    """

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

os.system("cls")

if age <= 6:
    print("The price is free!")
else:
    # Sunday, no upcharge
    if day_of_week == 1:
        upcharge = 0
    # Monday through Thursday, upcharge of 6
    elif 2 <= day_of_week <= 5:
        upcharge = 6
    # Friday and Saturday (The only 2 left), upcharge is 8
    else:
        upcharge = 8
    calculate_price(age, upcharge)
print("Thank you for your patronage!")

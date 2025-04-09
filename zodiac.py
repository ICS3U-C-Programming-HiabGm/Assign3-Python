# Created by: Hiab G
# Date: Wed, April. 9th
# This program gets users date of birth and month and tells you the zodiac sign fot that day and month

def main():
    print("Enter the date and month of birth to find out your zodiac sign!")
    
    try:

        # Get the player's guess

        month = int(input("Enter your birth month (1-12): "))
        day = int(input("Enter your birth day (1-31): "))


        sign = "Zodiacs"
        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            sign = "Capricorn"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            sign = "Sagittarius"
        if (month == 10 and day >= 23) or (month == 10 and day <= 22):
            sign = "Scorpio"
        if (month == 9 and day >= 23) or (month == 10 and day <= 22):
            sign = "Libra"
        if (month == 8 and day >= 23) or (month == 9 and day <= 22):
            sign = "Virgo"

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
        if (month == 7 and day >= 23) or (month == 8 and day <= 22):
            sign = "Leo"
        if (month == 6 and day >= 21) or (month == 7 and day <= 22):
            sign="Cance"
        if (month == 5 and day >= 21) or (month == 6 and day <= 20):
            sign = "Gemini"
        if (month == 4 and day >= 20) or (month == 5 and day <= 20):
            sign = "Taurus"
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            sign="Aries"
        if (month == 2 and day >= 19) or (month == 3 and day <= 20):
            sign="Pisces"
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            sign = "Taurus"
        
        if sign != (day > 1) or (day > 31) and (month < 1) or (month > 12):
            print("Invalid day and month! Please enter a day between 1-31 and a month between (1-12).")
        

    except Exception:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()

# Created by: Hiab G
# Date: Wed, April. 9th
# This program gets users date of birth and month and tells you the zodiac sign fot that day and month


def main():
    print("Enter your birthday to find out your zodiac sign!")

    try:

        month = int(input("Enter your birth month (1-12): "))
        day = int(input("Enter your birth day (1-31): "))

        # Validate input first
        if month < 1 or month > 12 or day < 1 or day > 31:
            print("Invalid date! Month must be 1-12 and day must be 1-31.")

        # Dates for zodiac signs
        sign = "Zodiacs"
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            sign = "Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            sign = "Pisces"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            sign = "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            sign = "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            sign = "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            sign = "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            sign = "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            sign = "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            sign = "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            sign = "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            sign = "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            sign = "Capricorn"

        print(f"Your zodiac sign is: {sign}")

    # Catch for Invalid input
    except Exception:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()

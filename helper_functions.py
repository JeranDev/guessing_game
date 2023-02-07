import random
import time


def insult(guess):
    insult = random.choice([0, 1, 2, 3])

    if insult == 0:
        try:
            guess = int(
                input(
                    "The wheel's spinning, but the hampster is dead... Keep guessing : "
                )
            )
            return guess
        except:
            print(f"Bitch, put a number")

    if insult == 1:
        try:
            guess = int(input("Sharp as a marble... Keep guessing : "))
            return guess
        except:
            print(f"Bitch, put a number")

    if insult == 2:
        try:
            guess = int(
                input("You're the reason we have warning labels... Keep guessing : ")
            )
            return guess
        except:
            print(f"Bitch, put a number")

    if insult == 3:
        try:
            guess = int(
                input(
                    "I can explain it again, but I can't understand it FOR you... Keep guessing : "
                )
            )
            return guess
        except:
            print(f"Bitch, put a number")


def restart():
    choice = input("Would you like to play again? YES/NO: ").upper()

    if choice != "YES" and choice != "NO":
        print("YES or NO dummy")
        return "TRY_AGAIN"

    elif choice == "YES":
        return "YES"

    elif choice == "NO":
        print("Goodbye")
        time.sleep(2)
        print("I secretly love you.")
        return

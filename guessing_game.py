# Made with minor annoyance by Jeran Burget
# Indentation in Python is ass

import random
import helper_functions


def game():
    number = random.randint(1, 10)
    counter = 0
    guess = None

    while guess != number:
        if guess is None:
            try:
                guess = int(
                    input(f"What number am I thinking of? It's between 1 and 10. : ")
                )
            except:
                print(f"Bitch, put a number")

        elif counter > 2:
            guess = helper_functions.insult(guess)
            counter = 0

        elif guess > number:
            if guess > 10:
                try:
                    guess = int(
                        input(
                            "Dude, learn to count. Enter a number that is less than 10 : "
                        )
                    )
                    counter += 1
                except:
                    print(f"Bitch, put a number")
            else:
                try:
                    guess = int(input("Too high, guess again. : "))
                    counter += 1
                except:
                    print(f"Bitch, put a number")

        elif guess < number:
            try:
                guess = int(input("Too low, guess again. : "))
                counter += 1
            except:
                print(f"Bitch, put a number")

    print(f"Wow, you guessed it! The number was {number}")

    play_again = helper_functions.restart()

    if play_again == "YES":
        game()


game()

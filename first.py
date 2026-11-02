
import random

print("Welcome to Number Guessing Game!")

again = "yes"

while again == "yes":

    number = random.randint(1, 100)

    count = 0
    chance = 5
    win = False

    print("\nA number between 1 and 100 has been selected.")
    print("You have 5 chances to guess the number.")

    while count < chance:

        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("Please enter numbers only!")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("The number must be between 1 and 100!")
            continue

        count = count + 1

        print("Attempt", count, "of 5")
        print("Remaining chances:", chance - count)

        if guess == number:

            print("\nCongratulations! You won!")
            win = True

            if count == 1:
                print("Your rank: Excellent!")

            elif count == 2:
                print("Your rank: Very Good!")

            elif count == 3:
                print("Your rank: Good!")

            elif count == 4:
                print("Your rank: Accepted!")

            else:
                print("Your rank: Lucky Winner!")

            break

        elif guess < number:

            difference = number - guess

            print("Try a bigger number!")

            if difference <= 5:
                print("Very close!")

            elif difference <= 15:
                print("Close, but still a little far!")

            else:
                print("Too far!")

        else:

            difference = guess - number

            print("Try a smaller number!")

            if difference <= 5:
                print("Very close!")

            elif difference <= 15:
                print("Close, but still a little far!")

            else:
                print("Too far!")

    if win == False:

        print("\nSorry! You lost!")
        print("The secret number was:", number)

    again = input("\nDo you want to play again? (yes/no): ")

    while again != "yes" and again != "no":

        print("Please enter yes or no only!")
        again = input("Do you want to play again? ")

print("\nGame Over! Thanks for playing!")

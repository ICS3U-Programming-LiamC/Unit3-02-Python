#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 10, 2021
# This program makes a random number and then has the user guess it

# this is a module that I found to generate random numbers
# found on
# https://www.programiz.com/python-programming/examples/random-number
import random


# this is the fucntion that does everything
def random_number_fun():
    # make the random number
    random_num = random.randint(0, 9)
    random_num = 6
    # just as a test to make sure it was working
    print(random_num)

    # get the users guess
    user_num = int(input("What do you think the number is: "))

# FIRST CHECKING #############

    # check if the user got it right
    if (user_num == random_num):
        print("\nCongratulations you got it right!")

    # check if the user got it wrong
    if (user_num != random_num):
        print("\nSorry you got it wrong")

        # CHECKING IF GREATER #############

        # if the users number was too big tell them
        if (user_num > random_num):
            print("Your number was too big")

            # and ask for their second guess
            user_num = int(input("Guess again: "))

            # if correct then congratulate
            if (user_num == random_num):
                print("\nCongratulations you got it right!")

            # if incorrect display correct answer
            if (user_num != random_num):
                print("\nSorry you got it wrong")
                print("The correct answer was {}".format(random_num))

        # CHECKING IF SMALLER #############

        # if the users number was too small
        if (user_num < random_num):
            print("Your number was too small")

            # ask them to guess again
            user_num = int(input("Guess again: "))

            # if correct then congratulate
            if (user_num == random_num):
                print("\nCongratulations you got it right!")

            # if incorrect display correct answer
            if (user_num != random_num):
                print("\nSorry you got it wrong")
                print("The correct answer was {}".format(random_num))


# initial bootup of the program
if __name__ == "__main__":
    random_number_fun()

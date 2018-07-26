####################################################################################################
# Copyright (c) Vyom Fadia. All rights reserved.
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
####################################################################################################

import random
import sys
import os

# Dictionary, translating the "r/p/s" choice into actual words, not currently in use.
RPS_literal = {"r": "rock", "p": "paper", "s": "scissors"}
# Dictionary to convert the r/p/s choice into numbers, for the maths bit in verifyWinner
RPS_mathematical = {"r": 0, "p": 1, "s": 2}


class Player(object):
    def __init__(self, name):
        self.lives = 3
        self.name = name
        self.points = 0

    def loseLife(self):  # Simple wrapper to take away a life from the user.
        self.lives -= 1

    def gainPoint(self):  # Simple wrapper to add a point to the user
        self.points += 1


class RPS(Player):
    def __init__(self, name):
        # Initialise the parent class. Read up on "Object-Oriented Inheritence"
        super(RPS, self).__init__(name)
        self.p1Input = None  # Create the variable.
        self.compInput = None  # Create the variable.

    def clearUp(self):
        # Set the value to none, so the userChoice does fool it's own way out.
        self.p1Input = None
        self.compInput = None  # Set this to none, just for continuity.

    def computerChoice(self):
        self.compInput = random.choice(["r", "p", "s"])

    def userChoice(self):
        # Keep asking until the user gives an actual input.
        while self.p1Input not in RPS_literal:
            self.p1Input = input(
                "Do you choose: Rock(r), Paper(p) or Scissors(s): ").lower()
            if self.p1Input == "":  # Check if the user even gave an input.
                print("You didn't choose anything. Please choose something :)")
            elif self.p1Input not in RPS_literal:  # Check if the user has given a valid input
                print("Invalid entry. Please choose one of the given choices.")

    def verifyWinner(self):
        '''
            This whole section relies on R = 0
                                         P = 1
                                         S = 2
            Follow along with the maths, to attempt
            understanding the mathematics behind this.
        '''
        p1Math = RPS_mathematical.get(self.p1Input, None)
        compMath = RPS_mathematical.get(self.compInput, None)

        if (p1Math+1) % 3 == compMath:
            # Make the user lose a life, once on 0, logic within the main while loop quits the game.
            self.loseLife()

            print("Sorry 'bout this. You lost. You now have %d lives left." % (self.lives))  # Print loss/win/draw to the terminal
        elif p1Math == compMath:  # If the two inputs match, it's clearly a draw.
            self.gainPoint()  # Give the user a point, doesn't do anything yet.

            # Print loss/win/draw to the terminal
            print("Ah shoot. You didn't win, you didn't lose though, so all's good!")
        else:
            # Print loss/win/draw to the terminal, this one wins by default.
            print("Wahoo! Well done, %s, you won!" % (self.name))

        self.clearUp()


def exit():
    print('\nBye Bye! See you later!!')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


if __name__ == "__main__":

    # Setting game as a variable, so checking if RPS is instantiated as game is possible.
    game = None

    while True:
        try:
            # Check if game is an instantiated object.
            if not isinstance(game, RPS):
                temp_name = input("Enter your name: ")

                # Instantiate RPS as 'game', passing the name just recorded as a parameter.
                game = RPS(temp_name)

                del temp_name  # Delete temp_name variable, cuz why not...

            elif game.lives == 0:  # Check if user is out of lives and exit the game.
                print("Oh no! %s, you have run out of lives! What will we do... Guess you'll have to try again later!" % (game.name))
                exit()

            elif isinstance(game, RPS):

                game.userChoice()
                game.computerChoice()
                game.verifyWinner()

                if input("Would you like to play again? Yes or No: ").lower() == "no":
                    break

        except KeyboardInterrupt:
            exit()

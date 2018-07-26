####################################################################################################  
# Copyright (c) Vyom Fadia. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
####################################################################################################

import random
import sys
import os

RPS_literal = {"r": "rock", "p": "paper", "s": "scissors"}
RPS_mathematical = {"r": 0, "p": 1, "s": 2}

class Player(object):
    def __init__(self, name):
        self.lives = 3
        self.name = name
        self.points = 0

    def loseLife(self):
        self.lives -= 1
    
    def gainPoint(self):
        self.points += 1

class RPS(Player):
    def __init__(self, name):
        super(RPS, self).__init__(name)
        self.p1Input = None
        self.compInput = None

    def clearUp(self):
        self.p1Input = None
        self.compInput = None

    def computerChoice(self):
        self.compInput = random.choice(["r", "p", "s"])
    
    def userChoice(self):
        while self.p1Input not in RPS_literal:
            self.p1Input = input(
                "Do you choose: Rock(r), Paper(p) or Scissors(s): ").lower()
            if self.p1Input == "":
                print("You didn't choose anything. Please choose something :)")
            elif self.p1Input not in RPS_literal:
                print("Invalid entry. Please choose one of the given choices.")
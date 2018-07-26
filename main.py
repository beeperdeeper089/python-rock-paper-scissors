####################################################################################################  
# Copyright (c) Vyom Fadia. All rights reserved.  
# Licensed under the MIT License. See LICENSE file in the project root for full license information.  
####################################################################################################

import random
import sys
import os


class Player(object):
    def __init__(self, name):
        self.lives = 3
        self.name = name
        self.points = 0

    def loseLife(self):
        self.lives -= 1
    
    def gainPoint(self):
        self.points += 1
"""
This module contains the WikiGame class, which is the main class for the Wiki Game. It is responsible for
playing the game and returning the path taken and the number of links clicked.
"""

from WikiGame.code.algorithms.Greedy import *
from WikiGame.code.algorithms.Backtrack import *
import requests

########################################################################################################################


class WikiGame:
    def __init__(self, origin, destination, algorithm, model):
        """
        The WikiGame class takes in a start URL, end URL, and algorithm and plays the Wiki Game.
        """
        if not self.validGame(origin, destination):
            raise ValueError("Invalid game. Please enter a valid start and end URL.")

        self.origin = origin
        self.destination = destination
        self.algorithm = algorithm
        self.model = model
        self.path = list()
        self.MAX_LINKS = 50

    def play_game(self):
        """
        play_game() plays the Wiki Game and returns the path taken and the number of links clicked.
        """

        if self.algorithm.lower() == "greedy":
            algorithm = Greedy(self.origin, self.destination, self.model)
        elif self.algorithm.lower() == "backtrack":
            algorithm = Backtrack(self.origin, self.destination, self.model)
        else:
            raise ValueError("Invalid algorithm. Please enter a valid algorithm.")

        self.path = algorithm.play(self.path)

        return self.path, len(self.path)

########################################################################################################################

    @staticmethod
    def validGame(origin, destination):
        """
        validGame() checks if the game is valid.
        """
        try:
            valid_link(origin)
        except requests.exceptions.RequestException:
            raise ValueError("Origin URL is not a valid Wikipedia page")

        try:
            valid_link(destination)
        except requests.exceptions.RequestException:
            raise ValueError("Destination URL is not a valid Wikipedia page")

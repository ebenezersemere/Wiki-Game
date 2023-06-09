"""
This module contains the WikiGame class, which is the main class for the Wiki Game. It is responsible for
playing the game and returning the path taken and the number of links clicked.
"""


try:
    from src.algorithms.Greedy import *
    from src.algorithms.Backtrack import *
    from src.api.api import valid_link
except Exception:
    pass

try:
    from WikiGame.src.algorithms.Greedy import *
    from  WikiGame.src.algorithms.Backtrack import *
    from  WikiGame.src.api.api import valid_link
except Exception:
    pass


import requests


########################################################################################################################


class WikiGame:
    def __init__(self, origin, destination, algorithm, model):
        """
        The WikiGame class takes in a start URL, end URL, and algorithm and plays the Wiki Game.
        """
        if not self.valid_game(origin, destination):
            raise ValueError("Invalid game. Please enter a valid start and end URL.")

        self.origin = origin
        self.destination = destination
        self.destination_page = get_page_contents(destination)
        self.algorithm = algorithm
        self.model = model
        self.path = list([origin])
        self.MAX_LINKS = 50

    def play_game(self):
        """
        play_game() plays the Wiki Game and returns the path taken and the number of links clicked.
        """
        """
        if self.algorithm.lower() == "greedy":
            algorithm = Greedy(self.origin, self.destination)
        elif self.algorithm.lower() == "backtrack":
            algorithm = Backtrack(self.origin, self.destination)
        else:
            raise ValueError("Invalid algorithm. Please enter a valid algorithm.")
            
        """
        algorithm =  self.algorithm(self.origin, self.destination,self.model, self.destination_page)

        if self.valid_game(self.origin, self.destination):
            self.path = algorithm.play(self.path)
        else:
            raise ValueError("Invalid game. Please enter a valid start and end URL.")

        return self.path, len(self.path)

########################################################################################################################

    @staticmethod
    def valid_game(origin, destination):
        """
        validGame() checks if the game is valid.
        """
        return (valid_link(origin)
                and valid_link(destination)
                and not is_redirect_page(origin)
                and not is_redirect_page(destination))


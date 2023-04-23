from WikiGame.code.algorithms.AlgorithmBase import AlgorithmBase
from WikiGame.code.algorithms.Algorithms import *

########################################################################################################################


class Greedy(AlgorithmBase):
    def __init__(self, origin, destination, model):
        super().__init__(origin, destination, model)

    def play(self, cur, path):
        hyperlinks = find_hyperlinks(cur)
        if self.destination in hyperlinks:
            path.append(self.destination)
            return path

        if len(path) > self.MAX_LINKS:
            print("Max links reached")
            return path

        closest = self.model.get_closest(hyperlinks, self.destination)

########################################################################################################################

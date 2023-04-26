from src.algorithms.AlgorithmBase import AlgorithmBase
from src.api.api import *
from src.models.WordVec import *
import pickle
import os

########################################################################################################################


class Greedy(AlgorithmBase):
    def __init__(self, origin, destination, model):
        super().__init__(origin, destination, model)

        if model == "WordVec":
            path = "data/glove.pickle"
            with open(path, "rb") as f:
                pickle_file = pickle.load(f)
            print("hi2")
            self.model = WordVec(pickle_file)
            

        else:
            raise ValueError("Invalid model. Please enter a valid model.")

    def play(self, path):
        cur = self.origin
        seen = set()

        while True:
            hyperlinks = find_hyperlinks(cur)

            # base case
            if self.destination in hyperlinks:
                path.append(self.destination)
                return path

            # if we have reached the max number of links, return
            if len(path) > self.MAX_LINKS:
                print("Max links reached")
                return path

            # find the top n closest hyperlinks
            closest = self.model.get_closest(hyperlinks, self.destination, 10)

            print(closest)

            # avoid cycles - find the first hyperlink that we haven't seen before
            for candidate in closest:
                if candidate not in seen and valid_link(candidate):
                    closest = candidate
                    break

            seen.add(closest)
            path.append(closest)


            cur = closest


########################################################################################################################

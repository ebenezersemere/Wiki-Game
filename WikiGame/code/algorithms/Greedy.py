from WikiGame.code.algorithms.AlgorithmBase import AlgorithmBase
from WikiGame.code.api.api import *
from WikiGame.code.models.WordVec import *

########################################################################################################################


class Greedy(AlgorithmBase):
    def __init__(self, origin, destination, model):
        super().__init__(origin, destination, model)

        if model == "WordVec":
            self.model = WordVec("WikiGame/data/word2vec/word2vec.txt")
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
            closest = self.model.query_n_closest(hyperlinks, self.destination, 10)

            print(closest)

            # avoid cycles - find the first hyperlink that we haven't seen before
            for candidate in closest:
                if candidate not in seen:
                    closest = candidate
                    break

            seen.add(closest)
            path.append(closest)

            cur = closest


########################################################################################################################

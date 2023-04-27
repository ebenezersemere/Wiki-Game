from WikiGame.code.api.api import *
from WikiGame.code.models.WordVec import *
import pickle


########################################################################################################################


class Greedy:
    def __init__(self, origin, destination, model):
        self.origin = origin
        self.destination = destination
        self.model = model
        self.path = list()
        self.cur = origin
        self.MAX_LINKS = 100
        self.abs_path = "/Users/ebenezersemere/Workspace/Pomona/Natural Language Processing/Final Project/WikiGame/data/glove.pickle"

        if model == "WordVec":
            with open(self.abs_path, "rb") as f:
                pickle_file = pickle.load(f)
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

            print(closest, ", candidates")

            # avoid cycles - find the first hyperlink that we haven't seen before
            for candidate in closest:
                if candidate not in seen and valid_link(candidate):
                    closest = candidate
                    break

            print(closest, ", choice")

            seen.add(closest)
            path.append(closest)

            cur = closest

########################################################################################################################

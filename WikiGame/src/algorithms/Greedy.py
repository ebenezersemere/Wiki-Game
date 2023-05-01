from WikiGame.src.api.api import *
from WikiGame.src.models.WordVec import *
import pickle
import os
from WikiGame.src.models.WordVec import *


########################################################################################################################


class Greedy:
    def __init__(self, origin, destination):
        self.blacklist = []
        self.origin = origin
        self.destination = destination
        self.seen = set()
        self.MAX_LINKS = 50

        # load the model
        pickle_path = ("/Users/ebenezersemere/Workspace/Student/Pomona"
                       "/Natural Language Processing/Final Project/WikiGame/data/glove.pickle")

        with open(pickle_path, 'rb') as f:
            data = pickle.load(f)

        self.model = WordVec(data)

    def play(self, path):

        def remove_blacklisted(hyperlinks):
            return [h for h in hyperlinks if not any(phrase in h for phrase in self.blacklist)]

        # avoid cycles - find the first hyperlink that we haven't seen before
        def get_next_page(hyperlinks):
            hyperlinks = remove_blacklisted(hyperlinks)
            closest_n = self.model.get_closest(hyperlinks, self.destination, 50)
            print(closest_n[:10])
            for candidate_and_sim in closest_n:
                # cand, sim = candidate_and_sim
                cand = candidate_and_sim

                if cand not in self.seen and valid_link(cand):
                    if self.model.count_vectorizable_documents(hyperlinks) > 0:
                        self.seen.add(cand)
                        return cand
            return None

        cur = self.origin

        while True:
            print()
            print("At", cur, "-->")
            hyperlinks = find_hyperlinks(cur)

            # base case
            if self.destination in hyperlinks:
                path.append(self.destination)
                return path

            # if we have reached the max number of links, return
            if len(path) > self.MAX_LINKS:
                print("Max links reached")
                return path

            next_page = get_next_page(hyperlinks)
            if not next_page:
                raise RuntimeError("Next page could not be found")
            path.append(next_page)
            cur = next_page

########################################################################################################################

try:
    from src.api.api import *
    from src.models.WordVec import *
    from src.models.WordVec import *
except Exception:
    pass

try:
    from WikiGame.src.api.api import *
    from WikiGame.src.models.WordVec import *
    from WikiGame.src.models.WordVec import *
except Exception:
    pass

import pickle
import os


########################################################################################################################


class Greedy:
    def __init__(self, origin, destination, model, destination_page):
        self.blacklist = []
        self.origin = origin
        self.destination = destination
        self.destination_page = destination_page
        self.seen = set()
        self.MAX_LINKS = 50

        self.model = model

    def play(self, path):

        def remove_blacklisted(hyperlinks):
            return [h for h in hyperlinks if not any(phrase in h for phrase in self.blacklist)]

        # avoid cycles - find the first hyperlink that we haven't seen before

        def get_next_page(hyperlinks):
            hyperlinks = remove_blacklisted(hyperlinks)
            closest_n = self.model.get_closest(hyperlinks, self.destination, 1000, self.destination_page)
            print(closest_n[:10])
            for candidate_and_sim in closest_n:
                # cand, sim = candidate_and_sim
                cand = candidate_and_sim

                if len(closest_n) == 1 or cand not in self.seen and valid_link(cand):
                    if is_redirect_page(cand) and find_hyperlinks(cand)[0] not in self.seen:
                        self.seen.add(cand)
                        print("Chose", find_hyperlinks(cand)[0])
                        return find_hyperlinks(cand)[0]

                    if self.model.count_vectorizable_documents(hyperlinks) > 0:
                        self.seen.add(cand)
                        print("Chose", cand)
                        return cand
            return None

        cur = self.origin

        while True:
            print()
            print("At", cur, "-->")
            hyperlinks = find_hyperlinks(cur)

            # base case
            if self.destination in hyperlinks or cur == self.destination:
                if cur == self.destination:
                    return path
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

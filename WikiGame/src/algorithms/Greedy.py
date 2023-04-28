from src.algorithms.AlgorithmBase import AlgorithmBase
from src.api.api import *
from src.models.WordVec import *
import pickle
import os

########################################################################################################################


class Greedy(AlgorithmBase):
    def __init__(self, origin, destination, model):
        super().__init__(origin, destination, model)
        self.destination_page = get_page_contents(destination)
        # Blacklist articles like 'Category:Articles lacking reliable references from December 2009'
        self.blacklist = ['Category:','Wikipedia:']
        self.seen = set()

        if model == "WordVec":
            path = "data/2MGloVe.pickle"
            with open(path, "rb") as f:
                pickle_file = pickle.load(f)
            self.model = WordVec(pickle_file)
            

        else:
            raise ValueError("Invalid model. Please enter a valid model.")

    def play(self, path):
        
        
        def remove_blacklisted(hyperlinks):
            return [h for h in hyperlinks if not any(phrase in h for phrase in self.blacklist)]
        
        # avoid cycles - find the first hyperlink that we haven't seen before
        def get_next_page(hyperlinks):
            hyperlinks = remove_blacklisted(hyperlinks)
            closest_n = self.model.get_closest(hyperlinks, self.destination + " "+ self.destination_page , 50)
            print(closest_n[:10])
            for candidate_and_sim in closest_n:
                cand, sim = candidate_and_sim
                

                
                if cand not in self.seen and valid_link(cand):
                    if self.model.count_vectorizable_documents(hyperlinks) > 0:
                        self.seen.add(cand)
                        return cand
            return None
                
        
        cur = self.origin

        while True:
            print()
            print(cur,"-->")
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
            if next_page is None:
                raise RuntimeError("Next page could not be found")
            path.append(next_page)
            cur = next_page


########################################################################################################################

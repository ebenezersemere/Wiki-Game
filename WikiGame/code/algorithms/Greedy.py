from WikiGame.code.algorithms.algorithms import *


def get_hyperlinks(cur_url):
    """
    get_hyperlinks() returns a list of hyperlinks from the current url.
    """
    return find_hyperlinks(cur_url)


class Greedy:
    def __init__(self, start, end, model):
        self.start = start
        self.cur = start
        self.end = end

        self.visited_urls = []
        self.model = model
        self.MAX_LINKS = 100

    def play_game(self):
        """
        # 1. need to get the hyperlinks of the current url
        2. need to get the next url
        3. need to visit the url
        4. need to check if the url is the end url
        5. need to check if the number of links is less than 100
        6. need to check if the url has been visited before
        7. need to add the url to the list of visited urls
        8. repeat until the end url is reached or the number of links is greater than 100
        """
        while self.cur != self.end and len(self.visited_urls) <= self.MAX_LINKS:
            hyperlinks = get_hyperlinks(self.cur)
            hyperlinks = clean_array(hyperlinks)

            # best_url = None
            # best_score = 0
            #
            # for url in hyperlinks:
            #     # score
            #
            # self.model.visit_url(self.cur)
            # self.cur = self.model.get_next_url()
            # self.visited_urls.append(self.cur)

        # while cur_url != self.destination and cur_links <= self.MAX_LINKS:
        #     self.algorithm.visit_url(cur_url)
        #     cur_url = self.algorithm.get_next_url()
        #     visited_urls.append(cur_url)
        #
        # return visited_urls, len(visited_urls)


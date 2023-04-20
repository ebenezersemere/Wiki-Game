"""
This module contains the WikiGame class, which is the main class for the Wiki Game. It is responsible for
playing the game and returning the path taken and the number of links clicked.
"""


class WikiGame:
    def __init__(self, origin, destination, algorithm):
        """
        The WikiGame class takes in a start URL, end URL, and algorithm and plays the Wiki Game.
        """
        self.origin = origin
        self.destination = destination
        self.algorithm = algorithm
        self.MAX_LINKS = 50

    def play_game(self):
        """
        play_game() plays the Wiki Game and returns the path taken and the number of links clicked.
        """
        cur_url = self.origin
        cur_links = 0
        visited_urls = []

        while cur_url != self.destination and cur_links <= self.MAX_LINKS:
            self.algorithm.visit_url(cur_url)
            cur_url = self.algorithm.get_next_url()
            visited_urls.append(cur_url)

        return visited_urls, len(visited_urls)

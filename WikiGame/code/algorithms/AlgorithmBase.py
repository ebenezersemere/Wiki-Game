from abc import ABC, abstractmethod

########################################################################################################################


class AlgorithmBase(ABC):
    """
    Interface for algorithms used in the Wiki Game.
    """

    def __init__(self, origin, destination, model):
        self.origin = origin
        self.destination = destination
        self.model = model
        self.path = list(origin)
        self.cur = origin
        self.MAX_LINKS = 100

    @abstractmethod
    def play(self, cur, path):
        """
        Plays the Wiki Game and updates the path.
        """
        pass

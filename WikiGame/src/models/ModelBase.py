# model base is the base class for the model

from abc import ABC, abstractmethod


class ModelBase(ABC):
    """
    Interface for models used in the Wiki Game.
    """

    def __init__(self):
        pass

    @abstractmethod
    def query(self, url):
        """
        Queries the model for the given URL.
        """
        pass

    @abstractmethod
    def get_closest(self, hyperlinks, destination):
        """
        Returns the closest URL to the given URL.
        """
        pass

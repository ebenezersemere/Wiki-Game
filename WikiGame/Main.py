from WikiGame.code.api.api import *
from WikiGame.code.game.WikiGame import *

if __name__ == "__main__":

    origin = input("Enter the origin page: ")
    while not valid_link(origin):
        print("Invalid link. Please enter a valid Wikipedia topic.")
        origin = input("Enter the origin page: ")

    destination = input("Enter the destination page: ")
    while not valid_link(destination):
        print("Invalid link. Please enter a valid Wikipedia topic.")
        destination = input("Enter the destination page: ")

    algorithm = input("Enter the algorithm: ")
    while not (algorithm == "Greedy" or algorithm == "Backtrack"):
        print("Invalid algorithm. Please enter 'Greedy' or 'Backtrack'.")
        algorithm = input("Enter the algorithm: ")

    model = input("Enter the model: ")
    while not (model == "WordVec"):
        print("Invalid model. Please enter 'WordVec'.")
        model = input("Enter the model: ")

    game = WikiGame(origin, destination, algorithm, model)
    path = game.play_game()

    print(f"Path taken: {path}")

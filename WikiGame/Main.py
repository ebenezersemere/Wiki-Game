from WikiGame.code.api.api import *
from WikiGame.code.game.WikiGame import *
from WikiGame.code.models.WordVec import WordVec

if __name__ == "__main__":
    # origin = input("Enter the origin page: ")
    # while not valid_link(origin):
    #     print("Invalid link. Please enter a valid Wikipedia topic.")
    #     origin = input("Enter the origin page: ")
    #
    # destination = input("Enter the destination page: ")
    # while not valid_link(destination):
    #     print("Invalid link. Please enter a valid Wikipedia topic.")
    #     destination = input("Enter the destination page: ")
    #
    # algorithm = input("Enter the algorithm: ")
    # while not (algorithm == "Greedy" or algorithm == "Backtrack"):
    #     print("Invalid algorithm. Please enter 'Greedy' or 'Backtrack'.")
    #     algorithm = input("Enter the algorithm: ")
    #
    # model = input("Enter the model: ")
    # while not (model == "WordVec"):
    #     print("Invalid model. Please enter 'WordVec'.")
    #     model = input("Enter the model: ")

    abs_path = "/Users/ebenezersemere/Workspace/Pomona/Natural Language Processing/Final Project/WikiGame/data/glove.pickle"

    with open(abs_path, "rb") as f:
        pickle_file = pickle.load(f)
    model = WordVec(pickle_file)

    links = find_hyperlinks("Dodgeball")
    r = model.get_closest(links, "Sports", 30)
    print(r)

    # origin = "Dodgeball"
    # destination = "Sports"
    # algorithm = "Greedy"
    # model = "WordVec"
    #
    # game = WikiGame(origin, destination, algorithm, model)
    # path = game.play_game()
    #
    # print(f"Path taken: {path}")

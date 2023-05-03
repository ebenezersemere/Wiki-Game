import sys

try:
    from src import *
except Exception:
    pass

try:
    from WikiGame.src import *
except Exception:
    pass

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        arg1 = sys.argv[1]
        arg2 = ' '.join(sys.argv[2:])
        print(f"Origin: {arg1}, Destination: {arg2}")
        banner_len = len(arg1) + len(arg2) + len("Origin: , Destination: ")
        print(banner_len * "-")
    else:
        raise ValueError('Invalid number of arguments. Usage: python script.py arg1 arg2')


    # load the model
    pickle_path = ("/Users/ebenezersemere/Workspace/Student/Pomona"
                   "/Natural Language Processing/Final Project/WikiGame/data/2Mglove.pickle")

    with open(pickle_path, 'rb') as f:
        data = pickle.load(f)

    model = WordVec(data)

    origin = arg1
    destination = arg2
    algorithm = Greedy

    game = WikiGame(origin, destination, algorithm, model)
    path = game.play_game()

    print(f"Path taken: {path}")

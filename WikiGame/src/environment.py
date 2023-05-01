# from WikiGame.src import *
#
# path = ("/Users/ebenezersemere/Workspace/Student/Pomona"
#         "/Natural Language Processing/Final Project/WikiGame/data/glove.pickle")
#
# # Open the file containing the pickled object
# with open(path, 'rb') as f:
#     # Load the pickled object from the file
#     data = pickle.load(f)
#
# model = WordVec(data)
#
# hyperlinks = find_hyperlinks("Computer science")
# # hyperlinks = clean_list(hyperlinks)
# print(hyperlinks)
# closest = model.get_closest(hyperlinks, "Rabbit", 5)
# print(closest)
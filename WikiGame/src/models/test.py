import pickle

# Open the file containing the pickled object
with open('top_50000.pickle', 'rb') as f:
    # Load the pickled object from the file
    my_object = pickle.load(f)


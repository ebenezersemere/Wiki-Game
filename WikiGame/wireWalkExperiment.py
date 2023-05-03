import networkx as nx
import matplotlib.pyplot as plt
import pickle
import time
import numpy as np
from gensim.models import Word2Vec
import json
import os
from joblib import Parallel, delayed
import math

start_time = time.time()
def preprocess_document(document, sentence_spliter='.', word_spliter=' ', punct_mark=','):
    # lowercase all words and remove trailing whitespaces
    document = document.lower().strip()
    
    # remove unwanted punctuation marks
    for pm in punct_mark:
        document = document.replace(pm, '')
    
    # get list of sentences which are non-empty
    sentences = [sent for sent in document.split(sentence_spliter) if sent != '']
    
    # get list of sentences which are lists of words
    document = []
    for sent in sentences:
        words = sent.strip().split(word_spliter)
        document.append(words)
        
    return document

def get_entities(document):
    # in our case, entities are all unique words
    unique_words = []
    for sent in document:
        for word in sent:
            if word not in unique_words:
                unique_words.append(word)
    return unique_words

def get_relations(document):
    # in our case, relations are bigrams in sentences
    bigrams = []
    for sent in document:
        for i in range(len(sent)-1):
            # for every word and the next in the sentence
            pair = [sent[i], sent[i+1]]
            # only add unique bigrams
            if pair not in bigrams:
                bigrams.append(pair)
    return bigrams

def build_graph(doc):
    # preprocess document for standardization
    pdoc = preprocess_document(doc)
    
    # get graph nodes
    nodes = get_entities(pdoc)
    
    # get graph edges
    edges = get_relations(pdoc)
    
    # create graph structure with NetworkX
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    return G

def build_digraph(doc):
    # preprocess document for standardization
    pdoc = preprocess_document(doc)
    
    # get graph nodes
    nodes = get_entities(pdoc)
    
    # get graph edges
    edges = get_relations(pdoc)
    
    # create graph structure with NetworkX
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    return G

def get_weighted_edges(document):
    # in our case, relations are bigrams in sentences
    # weights are number of equal bigrams
    # use a dict to store number of counts
    bigrams = {}
    for sent in document:
        for i in range(len(sent)-1):
        
            # transform to hashable key in dict
            pair = str([sent[i], sent[i+1]])
            
            if pair not in bigrams.keys():
                # weight = 1
                bigrams[pair] = 1
            else:
                # already exists, weight + 1
                bigrams[pair] += 1
                
    # convert to NetworkX standard form each edge connecting nodes u and v = [u, v, weight]
    weighted_edges_format = []
    for pair, weight in bigrams.items():
        # revert back from hashable format
        w1, w2 = eval(pair)
        weighted_edges_format.append([w1, w2, weight])
        
    return weighted_edges_format

def build_weighted_digraph(document):
    # preprocess document for standardization
    pdoc = preprocess_document(document)
    
    # get graph nodes
    nodes = get_entities(pdoc)
    
    # get weighted edges
    weighted_edges = get_weighted_edges(pdoc)
    
    # create graph structure with NetworkX
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(weighted_edges)
    
    return G

def salton_index(G, current_node, destination):
    if current_node != destination:
        curr = list(G.neighbors(current_node))
        dest = list(G.neighbors(destination))
        denominator = math.sqrt(len(curr)*len(dest))
        if denominator == 0:
            ss_weight = 0
        else:
            numerator = len(set(curr+dest))
            ss_weight = numerator/denominator
    else:
        ss_weight = 0
    return ss_weight 


def speed_up(G, num_workers, transition_matrix_function):
    nodes = G.nodes
    # Split the nodes into chunks for each worker
    node_chunks = np.array_split(nodes, num_workers)

    # Use joblib to parallelize the calculation of ss_weight
    ss_weights = Parallel(n_jobs=num_workers)(
        delayed(transition_matrix_function)(G, current_node, destination)
        for chunk in node_chunks
        for current_node in chunk
        for destination in nodes
    )

    # Reshape the ss_weights list into a matrix
    ss_weights_matrix1 = np.reshape(ss_weights, (len(nodes), len(nodes)))
    # ss_weights_matrix1 = ss_weights_matrix1/ss_weights_matrix1.sum(axis=1, keepdims=True)


    # check if row sums are zero
    row_sums = ss_weights_matrix1.sum(axis=1)
    zero_rows = np.where(row_sums == 0)[0]

    # set all elements in zero rows to zero, except for diagonal element
    ss_weights_matrix1[zero_rows, :] = 0
    for i in zero_rows:
        ss_weights_matrix1[i, i] = 1

    row_sums = ss_weights_matrix1.sum(axis=1)
    # normalize matrix by row sums
    ss_weights_matrix1 = np.divide(ss_weights_matrix1, row_sums[:, np.newaxis])
    return ss_weights_matrix1

def generate_walks(graph, num_walks, walk_length, transition_probs, num_jobs=-1):
    walks = []
    nodes = list(graph.nodes())

    # Convert the transition probabilities to a dictionary of dictionaries for faster access
    probs = {}
    for i, node_i in enumerate(nodes):
        probs[node_i] = {}
        for j, node_j in enumerate(nodes):
            probs[node_i][node_j] = transition_probs[i][j]

    def generate_walks_for_node(node):
        node_walks = []
        for walk in range(num_walks):
            walk_list = [node]
            for step in range(walk_length - 1):
                neighbors = list(probs[walk_list[-1]].keys())
                probabilities = list(probs[walk_list[-1]].values())
                next_node = np.random.choice(neighbors, p=probabilities)
                walk_list.append(next_node)
            node_walks.append(walk_list)
        return node_walks

    node_walks_list = Parallel(n_jobs=num_jobs)(
        delayed(generate_walks_for_node)(node) for node in nodes)

    for node_walks in node_walks_list:
        walks += node_walks

    return walks

def getnet(G,func,num_walks=10, walk_length=80, num_workers=4, window=10,dimension=128):
    func_name = str(func).split()[1]
    print(f"Computing {func_name} transition matrix")
    ss_weights_matrix = speed_up(G,num_workers,func)
    print(f"Computing {func_name} walks")
    walks = generate_walks(G, num_walks=num_walks, walk_length=walk_length, transition_probs = ss_weights_matrix)
    print(f"Computing {func_name} model")
    model = Word2Vec(walks, window=window, workers=num_workers, vector_size=dimension)
    emb=model.wv[[i for i in model.wv.key_to_index]]
    model.save(f"my_{func_name}_model")
    return model

print("Reading file")  
content = ""
with open('normal.s16.txt', 'r') as f:
#     content = f.read(10000).replace('\n', '')
    for i,line in enumerate(f):
        if i < 10:
            content += line.replace("\n", "")

print("Building graph")
g = build_graph(content)
print("Saving graph")
pickle.dump(g, open('g.pickle', 'wb'))
end_time = time.time()
time_elapsed = end_time - start_time
print(time_elapsed)

            # dig = build_digraph(content)
            # print("Saving graph")
            # pickle.dump(dig, open('dig.pickle', 'wb'))
            # end_time = time.time()
            # time_elapsed = end_time - start_time
            # print(time_elapsed)
            # wdig = build_weighted_digraph(content)
            # print("Saving graph")
            # pickle.dump(wdig, open('wdig.pickle', 'wb'))
            # end_time = time.time()
            # time_elapsed = end_time - start_time
            # print(time_elapsed)

            # print("Saving graph")
            # # save graph object to file
            # pickle.dump(g, open('g.pickle', 'wb'))
            # pickle.dump(dig, open('dig.pickle', 'wb'))
            # pickle.dump(wdig, open('wdig.pickle', 'wb'))

            # end_time = time.time()
            # time_elapsed = end_time - start_time
            # print(time_elapsed)



# load graph object from file
G = pickle.load(open('g.pickle', 'rb'))
print(nx.info(G)) 
workers = os.cpu_count()
model = getnet(G, salton_index, num_walks=10, walk_length=80, num_workers=workers, window=10,dimension=128)
keys = model.wv.key_to_index.keys()
entry = {}
for key in keys:
    entry[key] = model.wv.get_vector(key)

# Open a file to save the pickle
with open('wirewalk.pickle', 'wb') as f:
    # Dump the dictionary to the file
    pickle.dump(entry, f)
    
with open('normal.s16.txt', 'r') as f:
    lines = f.readlines()[:10]

model = Word2Vec(lines, window=10, workers=workers, vector_size=128)
keys = model.wv.key_to_index.keys()
entry = {}
for key in keys:
    entry[key] = model.wv.get_vector(key)

# Open a file to save the pickle
with open('word2vec.pickle', 'wb') as f:
    # Dump the dictionary to the file
    pickle.dump(entry, f)
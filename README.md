# Wiki-Game

Wiki Game is a hyper-textual, Wikipedia-based online game with a simple
premise: navigate from an origin page to a destination page, traversing from
one article to the next through intermediary links. The goal is to reach the
destination page in as few intermediary links as possible.

One strategy is to choose the link that most closely associates with the
destination page. The task of finding this choice is well suited to techniques of
natural language processing, specifically word similarity. With these techniques,
we hope to build a program that informs a strategy for the Wiki Game.

The program will implement techniques related to word vectors and word
similarity. We will tune our program using a variety of metrics across two different vectorization techniques: 
word vectorization models & a novel implemention (named metric2vec). 
The aim of this program is to outperform human players on the online platform.
from scipy import spatial


class WordVec:
    def __init__(self, word_vectors):
        """
        Initializes a new WordVec instance with a given dictionary of word vectors.

        :param word_vectors: A dictionary of word vectors.
        """
        self.word_vecs = word_vectors

    def _find_average_word_vec(self, word_list):
        word_vecs = []
        for word in set(word_list):
            if word in self.word_vecs:
                word_vecs.append(self.word_vecs[word])

        if len(word_vecs) == 0:
            raise ValueError("Text contains no words in vocabulary")
        return sum(word_vecs)/len(word_vecs)

    def get_closest(self, documents, comparison_document, n):
        """
        Finds the n closest documents to a given comparison document based on their similarity to it.
        In our use case, each document will be the title of a wiki article.
        :param comparison_document: The comparison document.
        :param n: The number of closest documents to return.
        :return: The n closest documents to the comparison document.
        """
        def sim(vec1, vec2):
            return 1 - spatial.distance.cosine(vec1, vec2)

        comparison_vec = self._find_average_word_vec(comparison_document)

        doc_vec = {}
        for doc in documents:
            doc_word_list = doc.split()
            doc_vec[doc] = self._find_average_word_vec(doc_word_list)

        return sorted(documents, key=lambda doc: sim(doc_vec[doc], comparison_vec))[:n]


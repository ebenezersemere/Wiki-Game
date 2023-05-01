from scipy import spatial
import nltk


class WordVec:
    def __init__(self, word_vectors):
        """
        Initializes a new WordVec instance with a given dictionary of word vectors.

        :param word_vectors: A dictionary of word vectors.
        """

        nltk.download('stopwords')
        # from nltk.corpus import stopwords
        self.word_vecs = word_vectors
        self.stop_words = set()  # set(stopwords.words('english'))

    def _split_and_clean(self, document, exclude_documents_with_OOV_words=True):
        ret = []
        for word in document.split():
            # If upper case not in vocab, then try lowercasing
            if word not in self.word_vecs:
                word = word.lower()
            
            if exclude_documents_with_OOV_words:
                # if at least one word is not in vocab, don't return any words
                if word not in self.word_vecs:
                    return []
        
            # filter stop words
            if word not in self.stop_words and word in self.word_vecs:
                ret.append(word)
        return ret

    def _find_average_word_vec(self, word_list):
        word_vecs = []
        for word in set(word_list):
            if word not in self.word_vecs:
                raise ValueError("Text contains out of vocab words")

            word_vecs.append(self.word_vecs[word])

            if word in self.word_vecs:
                word_vecs.append(self.word_vecs[word])

        if len(word_vecs) == 0:
            raise ValueError("Text contains no words in vocabulary")
        return sum(word_vecs) / len(word_vecs)

    def count_vectorizable_documents(self, documents):
        cleaned = [self._split_and_clean(doc) for doc in documents]
        non_empty = [x for x in cleaned if len(x) > 0]
        return len(non_empty)

    def get_closest(self, documents, comparison_document, n, comparison_document_page=""):
        """
        Finds the n closest documents to a given comparison document based on their similarity to it.
        In our use case, each document will be the title of a wiki article.
        :param documents: A list of strings.
        :param comparison_document: a string.
        :param n: The number of closest documents to return.
        :return: The n closest documents to the comparison document.

        Example:
        a = WordVec(embeddings)
        documents = ["hi cat dog", "child son", "son", "child", "doc2 mom dad","trees are cool", "haha", "house","home", "Unfortunately no. This is a federally funded program and thus only US citizens and permanent residents are elligible to apply."]
        comp = "son"
        a.get_closest(documents,comp,4)
        Output: ['son', 'child son', 'doc2 mom dad', 'child']
        """

        def sim(vec1, vec2):
            return 1 - spatial.distance.cosine(vec1, vec2)

        if comparison_document in documents:
            return [comparison_document]

        # Compute comparison vector
        comp_words_clean = self._split_and_clean(comparison_document)
        
        if len(comp_words_clean) == 0:
            comp_words_clean = self._split_and_clean(comparison_document +" "+ comparison_document_page,
                                                     exclude_documents_with_OOV_words= False)
        
        if len(comp_words_clean) == 0:
            raise ValueError("Comparison document only contains out of vocab words")
        comparison_vec = self._find_average_word_vec(comp_words_clean)

        # Compute document vectors
        doc_vecs = {}
        for doc in documents:
            clean_split_doc = self._split_and_clean(doc)
            if len(clean_split_doc) > 0:
                doc_vecs[doc] = self._find_average_word_vec(clean_split_doc)


        if len(doc_vecs) == 0:
            raise ValueError("No document vectors could be computed")

        in_vocab_doc = doc_vecs.keys()


        return sorted(in_vocab_doc, key=lambda doc: sim(doc_vecs[doc], comparison_vec), reverse=True)[:n]

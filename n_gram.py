from data_processor.elastic_search import ElasticSearch
import re
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.probability import FreqDist
from nltk.metrics import BigramAssocMeasures
import numpy as np
import codecs

#==== General parameters
FEATURES_NUMBER = 10000
NGRAMS_NUMBER = 2

#==== Text processing constants
BLACKLIST_STOPWORDS = ['over','only','very','not','no']
ENGLISH_STOPWORDS = set(stopwords.words('english')) - set(BLACKLIST_STOPWORDS)
NEG_CONTRACTIONS = [
    (r'aren\'t', 'are not'),
    (r'can\'t', 'can not'),
    (r'couldn\'t', 'could not'),
    (r'daren\'t', 'dare not'),
    (r'didn\'t', 'did not'),
    (r'doesn\'t', 'does not'),
    (r'don\'t', 'do not'),
    (r'isn\'t', 'is not'),
    (r'hasn\'t', 'has not'),
    (r'haven\'t', 'have not'),
    (r'hadn\'t', 'had not'),
    (r'mayn\'t', 'may not'),
    (r'mightn\'t', 'might not'),
    (r'mustn\'t', 'must not'),
    (r'needn\'t', 'need not'),
    (r'oughtn\'t', 'ought not'),
    (r'shan\'t', 'shall not'),
    (r'shouldn\'t', 'should not'),
    (r'wasn\'t', 'was not'),
    (r'weren\'t', 'were not'),
    (r'won\'t', 'will not'),
    (r'wouldn\'t', 'would not'),
    (r'ain\'t', 'am not') # not only but stopword anyway
]
OTHER_CONTRACTIONS = {
    "'m": 'am',
    "'ll": 'will',
    "'s": 'has', # or 'is' but both are stopwords
    "'d": 'had'  # or 'would' but both are stopwords
}


class Extractor(object):

    def __init__(self, training_set):
        """
        Init the SentimentMachine with the training set.

        Args:
            training_set: A list of documents (list of strings)
            score_set: A list of sentiment scores (list of numbers)

            len(training_set) and len(score_set) must be equal.
        """
        self.training_set = training_set
        self.stemmer = PorterStemmer()
        # dictionnary of sets of ngrams
        self._most_common_ngrams = {}

    def clean_str(self, doc):

        doc = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', doc)
        doc = re.sub(r'[0-9]+', '', doc)

        return doc

    def compute_ngrams(self, document, n):
        """
        Compute ngrams of the document.

        Args:
            document: The document as a string.
            n: The number of grams. Must be a positive interger.

        Returns:
            A list of ngrams.
        """
        # lowercase
        doc = document.lower()

        # pre-processing
        # doc = self.clean_str(doc=doc)

        # TODO split by sentences for more accuracy
        # transform negative contractions (e.g don't --> do not)
        for t in NEG_CONTRACTIONS:
            doc = re.sub(t[0], t[1], doc)
        # tokenize
        tokens = word_tokenize(doc)
        # transform other contractions (e.g 'll --> will)
        tokens = [OTHER_CONTRACTIONS[token] if OTHER_CONTRACTIONS.get(token)
                  else token for token in tokens]
        # remove punctuation
        r = r'[a-z]+'
        tokens = [word for word in tokens if re.search(r, word)]

        # remove irrelevant stop words
        tokens = [token for token in tokens if token not in ENGLISH_STOPWORDS]
        # stemming
        tokens = [self.stemmer.stem(token) for token in tokens]
        if n == 1:
            # return the list of words
            return tokens
        else:
            # return the list of ngrams
            return ngrams(tokens, n)

    def get_most_common_ngrams(self, n, nb_ngrams=None):
        """
        Compute and return the set of the most common ngrams in the documents.
        This set is cached inside the object.

        Args:
            n: The number of grams. Must be a positive interger.
            nb_ngrams: The number of ngrams to return, i.e quantifying the 'most'.

        Returns:
            A list of the most common ngrams.
        """
        try:
            # return cached value
            return self._most_common_ngrams[n]
        except KeyError:
            pass

        # compute all ngrams
        all_ngrams = []
        for document in self.training_set["hits"]["hits"]:
            if document["_source"]["external_review_report"] is not None:
                all_ngrams.extend(self.compute_ngrams(document["_source"]["external_review_report"], n))
            if document["_source"]["external_review_form"] is not None:
                all_ngrams.extend(self.compute_ngrams(document["_source"]["external_review_form"], n))


        # get the frequency or return all ngrams
        freq = FreqDist(ngram for ngram in all_ngrams)
        # store and return the nb_ngrams most common ngrams
        word_scores = {}
        if nb_ngrams:
            self._most_common_ngrams[n] = freq.keys()[:nb_ngrams]
            for word, freqs in freq.iteritems():
                score = BigramAssocMeasures.chi_sq(freq[word], (freqs, freq.N()), freq.N() + freq.N())
                word_scores[word] = score

            self.best = []
            self.best = sorted(word_scores.iteritems(), key=lambda (w, s): s, reverse=True)[:n]
            self.bestwords = set([w for w, s in self.best])
        else:
            self._most_common_ngrams[n] = freq.keys()
        return self.bestwords #self._most_common_ngrams[n]

    def document_features(self, document):
        """
        Compute the nb features of a given document.
         - most common words: 1 if the document contains this word, else 0
         - most common bigrams: 1 if the document contains this bigram, else 0

         Args:
            document: The document as a string.

        Returns:
            A list of binary features.
        """
        features = []

        # most common ngrams for n = 1 to NGRAMS_NUMBER
        nb_ngrams = NGRAMS_NUMBER
        nb_features = FEATURES_NUMBER / nb_ngrams

        for n in range(nb_ngrams):
            # common_ngrams = []
            ngram_words = []
            # get ngrams in the document
            if document["_source"]["external_review_report"] is not None:
                ngrams_report = set(self.compute_ngrams(document["_source"]["external_review_report"], n + 1))
            if document["_source"]["external_review_form"] is not None:
                ngrams_form = set(self.compute_ngrams(document["_source"]["external_review_form"], n + 1))
            for ngram in self.get_most_common_ngrams(n + 1, nb_features):
                # # if ngram is a common one then feature = 1 else 0
                # common_ngrams.append(1 if ngram in ngrams_report else 0)
                try:
                    if ngram in ngrams_report:
                        ngram_words.append(ngram)
                except:
                    pass
                try:
                    if ngram in ngrams_form:
                        ngram_words.append(ngram)
                except:
                    pass

            # add new feature
            features.extend(ngram_words)

        return features

    def write_file(self, file_name, data):
        with codecs.open(file_name, "w", encoding="utf-8") as f:
            for row in data:
                for words in row:
                    if len(words) == 2:
                        for word in words:
                            f.write(word + ' ')
                    else:
                        f.write(words)
                    f.write('\t\t')
                f.write('\n')
        f.close()
if __name__ == '__main__':

    es = ElasticSearch()
    status = es.check_node_status()
    if status != None:
        es.connect_es()

    training_data = es.get_all_document(index="green_bond", doc="report")
    extractor = Extractor(training_data)
    m = []
    for row in training_data["hits"]["hits"]:
        m.append(extractor.document_features(row))
    extractor.write_file("ngrams.txt", m)
    p = np.array(m)
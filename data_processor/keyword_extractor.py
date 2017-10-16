import data_helper
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
import json
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

# start class
class KeywordExtractor(object):
    # variables
    # start __init__
    def __init__(self, trainingData):
        # Instantiate classifier helper
        self.helper = data_helper.DataHelper()
        self.trainingData = trainingData

    def getBestwords(self):
        sentences = self.getTrainedData(self.trainingData)
        word_fd = FreqDist()
        label_word_fd = ConditionalFreqDist()

        for words in sentences:
            for word in words:
                word_fd[word.lower()] += 1
                label_word_fd['best'][word.lower()] += 1

        word_count = label_word_fd['best'].N()
        total_word_count = word_count + word_count

        word_scores = {}

        for word, freq in word_fd.iteritems():
            score = BigramAssocMeasures.chi_sq(label_word_fd['best'][word], (freq, word_count), total_word_count)
            word_scores[word] = score

        self.best = []
        self.best = sorted(word_scores.iteritems(), key=lambda (w, s): s, reverse=True)[:5000]
        self.bestwords = set([w for w, s in self.best])
        return self.best

    def getUnigramFeature(self):
        words = self.getBestwords()
        bestWords = dict([(w, p) for w, p in words])
        return bestWords

    def getBigramFeature(self, bestWords):
        d = self.best_bigram_word_feats(bestWords)
        return d

    def best_word_feats(self, words):
        return dict([(word, True) for word in words if word in words])

    def best_bigram_word_feats(self, words, score_fn=BigramAssocMeasures.chi_sq, n=1000):
        bgm = BigramAssocMeasures()
        bigram_finder = BigramCollocationFinder.from_words(words)
        self.bigrams = bigram_finder.score_ngrams(bgm.likelihood_ratio)
        # self.bigrams = bigram_finder.nbest(score_fn, n)
        d = dict([(' '.join(bigram), s) for bigram, s in self.bigrams])
        # d.update(self.best_word_feats(words))
        return d

    # start getProcessedSentence
    def getProcessedSentences(self, data):
        sentences = {}
        for i in data:
            d = data[i]
            tw = []
            for t in d:
                words = self.helper.process_sentence(t)
                words_filtered = [e.lower() for e in words.split() if (self.helper.is_ascii(e))]
                words_filtered = [self.helper.replaceTwoOrMore(word) for word in words_filtered]
                tw.append(words_filtered)
            sentences[i] = tw
        # end loop
        return sentences

    # end

    def getTrainedData(self, trainingData):
        # read all data
        sentenceItems = self.getFilteredTrainingData(trainingData)

        sentences = []
        for words in sentenceItems:
            words_filtered = [e.lower() for e in words.split() if (self.helper.is_ascii(e))]
            words_filtered = [self.helper.replaceTwoOrMore(word) for word in words_filtered]
            sentences.append(words_filtered)

        return sentences

    # start getFilteredTrainingData
    def getFilteredTrainingData(self, trainingData):

        sentenceItems = []
        count = 1
        for row in trainingData:
            if row["_source"]["external_review_report"] is None:
                continue
            lines = row["_source"]["external_review_report"].split('\n')
            for line in lines:
                line = self.helper.clean_str(line)
                processed_sentence = self.helper.process_sentence(line)
                if processed_sentence != '':
                    sentence_item = processed_sentence
                    sentenceItems.append(sentence_item)
                    count += 1
            # processed_sentence = self.helper.process_sentence(row["_source"]["external_review_report"])
            # processed_sentence = self.helper.clean_str(row["_source"]["external_review_report"])
            # sentence_item = processed_sentence
            # sentenceItems.append(sentence_item)
            # count += 1
        # end loop
        return sentenceItems

    # end

    def get_bigrams(self, myString):
        tokenizer = WordPunctTokenizer()
        tokens = tokenizer.tokenize(myString)

        bigram_finder = BigramCollocationFinder.from_words(tokens)
        bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 500)

        for bigram_tuple in bigrams:
            x = "%s %s" % bigram_tuple
            tokens.append(x)

        result = [' '.join([w.lower() for w in x.split()]) for x in tokens if
                  x.lower() not in stopwords.words('english') and len(x) > 8]
        return result

    def write_file(self, file_name, data):
        f = open(file_name, 'w')
        for row in data:
            f.write(row + '\n')
        f.close()

import re
from nltk.corpus import stopwords


class DataHelper:
    # start __init__
    def __init__(self):
        self.wordFeatures = []
        self.cachedStopWords = stopwords.words("english")
    # end

    # start replaceTwoOrMore
    def replaceTwoOrMore(self, s):
        # pattern to look for three or more repetitions of any character, including
        # newlines.
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)

    # end
    def clean_str(self, string, TREC=False):
        """
        Tokenization/string cleaning for all datasets except for SST.
        Every dataset is lower cased except for TREC
        """
        string  = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', string)
        string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
        string = re.sub(r"\'s", " \'s", string)
        string = re.sub(r"\'ve", " \'ve", string)
        string = re.sub(r"n\'t", " n\'t", string)
        string = re.sub(r"\'re", " \'re", string)
        string = re.sub(r"\'d", " \'d", string)
        string = re.sub(r"\'ll", " \'ll", string)
        string = re.sub(r",", " , ", string)
        string = re.sub(r"!", " ! ", string)
        string = re.sub(r"\(", " \( ", string)
        string = re.sub(r"\)", " \) ", string)
        string = re.sub(r"\?", " \? ", string)
        string = re.sub(r"\s{2,}", " ", string)
        return string.strip() if TREC else string.strip().lower()

    # start process_tweet
    def process_sentence(self, sentence):
        # Conver to lower case
        sentence = sentence.lower()
        #remove url
        sentence = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', sentence)
        # Remove additional white spaces
        sentence = re.sub('[\s]+', ' ', sentence)
        # Replace #word with word
        sentence = re.sub(r'#([^\s]+)', r'\1', sentence)
        sentence = re.sub('[!\?.,#]', '', sentence)
        # trim
        sentence = sentence.strip()
        # remove first/last " or 'at string end
        sentence = sentence.rstrip('\'"')
        sentence = sentence.lstrip('\'"')
        sentence = sentence.strip('!')
        sentence = sentence.strip('.')
        sentence = sentence.strip('?')
        sentence = sentence.strip(',')
        sentence = sentence.strip('#')
        sentence = sentence.rstrip(';')

        sentence = re.sub('[(,),",\',%,:,-]', '', sentence)
        sentence = re.sub('[0-9]', '', sentence)

        sentence = ' '.join([word for word in sentence.split() if (word not in self.cachedStopWords)])

        return sentence
    # end

    # start is_ascii
    def is_ascii(self, word):
        return all(ord(c) < 128 for c in word)

    # end

    def split(self, str):
        return str[0].split('_')

# end class

from data_processor.data_loader import DataLoader
from data_processor.keyword_extractor import KeywordExtractor
from data_processor.elastic_search import ElasticSearch

import nltk, re, pprint
from nltk import word_tokenize, wordpunct_tokenize

if __name__ == '__main__':
    data = DataLoader("./data/raw_data/")
    # data.read_excel_file()
    data.read_excel_file_data()
    # es = ElasticSearch()
    # status = es.check_node_status()
    # if status != None:
    #     es.connect_es()
    # training_data = es.get_all_document(index="green_bond", doc="report")
    # keyword_extractor = KeywordExtractor(training_data["hits"]["hits"])
    # words = keyword_extractor.getUnigramFeature()
    # keyword_extractor.write_file("unigram.txt", words)
    # bigrams = keyword_extractor.getBigramFeature(keyword_extractor.bestwords)
    # keyword_extractor.write_file("bigram.txt", bigrams)

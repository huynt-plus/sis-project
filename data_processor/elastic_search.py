import requests
from elasticsearch import Elasticsearch

class ElasticSearch(object):
    def check_node_status(self):
        res = requests.get('http://localhost:9200')
        if res.status_code == 200:
            return (res.content)
        return None

    def connect_es(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def add_document(self,id, data):
        self.es.index(index='green_bond', doc_type='report', id=id, body=data)

    def update_document(self, index, doc, id, data):
        self.es.delete(index=index, doc_type=doc, id=id)
        self.add_document(id, data)

    def check_document_exists(self, index, doc, id):
        return self.es.exists(index=index,doc_type=doc,id=id)

    def find_document(self, index, doc, id):
        return self.es.get(index=index, doc_type=doc, id=id)

    def get_all_document(self, index, doc):
        return self.es.search(index = index, doc_type = doc, size=1000, pretty=1)
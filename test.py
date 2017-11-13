from data_processor.elastic_search import ElasticSearch
import codecs

def write_file(file_name, data):
    with codecs.open(file_name, "w", encoding="utf-8") as f:
        f.write(data)
    f.close()

es = ElasticSearch()
status = es.check_node_status()
if status != None:
    es.connect_es()
documents = es.get_all_document(index="green_bond", doc="report")
for doc in documents["hits"]["hits"]:
    try:
        # doc = es.find_document(index="green_bond", doc="report", id=document["_id"])
        write_file("./data/raw_data/REPORT_TXT/" + doc["_source"]["orginal_file"] + "_report.txt", doc["_source"]["external_review_report"])
        write_file("./data/raw_data/REPORT_TXT/" + doc["_source"]["orginal_file"] + "_form.txt", doc["_source"]["external_review_form"])
    except:
        write_file("./data/raw_data/REPORT_TXT/UNKNOWN" + "_report.txt",
                   doc["_source"]["external_review_report"])
        write_file("./data/raw_data/REPORT_TXT/UNKNOWN" + "_form.txt",
                   doc["_source"]["external_review_form"])
        pass
# import libraries
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

# starting time
start_time = time.time()

# program body starts
res = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "mod*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res2 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "diffe*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res3 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "effe*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res4 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "pat*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res5 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "sign*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res6 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "prese*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res7 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "usi*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res8 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "spec*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res9 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "dat*","fields": ["title", "abstract"]}}}, request_timeout=2000)
res10 = es.search(index="crossref_total500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"query_string":{"query": "prop*","fields": ["title", "abstract"]}}}, request_timeout=2000)
# program body ends

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

result = [res, res2, res3, res4, res5, res6, res7, res8, res9, res10]
for x in result:
    print(x)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")
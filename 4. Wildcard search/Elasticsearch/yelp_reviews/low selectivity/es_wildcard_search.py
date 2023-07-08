# import libraries
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()

# starting time
start_time = time.time()

# program body starts
res = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"sta*"}}}, request_timeout=2000)
res2 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"grea*"}}}, request_timeout=2000)
res3 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"ver*"}}}, request_timeout=2000)
res4 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"servic*"}}}, request_timeout=2000)
res5 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"rea*"}}}, request_timeout=2000)
res6 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"tim*"}}}, request_timeout=2000)
res7 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"ever*"}}}, request_timeout=2000)
res8 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"get*"}}}, request_timeout=2000)
res9 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"lik*"}}}, request_timeout=2000)
res10 = es.search(index="yelp_review500", body={"from":0, "size":0, "track_total_hits" : True, "query":{"wildcard":{"review":"some*"}}}, request_timeout=2000)
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
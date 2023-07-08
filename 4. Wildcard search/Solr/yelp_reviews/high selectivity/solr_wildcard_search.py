# import libraries
import urllib.request
from urllib.request import urlopen
import time

# starting time
start_time = time.time()

connection = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Aflower*&wt=python')
response = eval(connection.read())
print (response['response']['numFound'], "documents found")
connection2 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Acelebrati*&wt=python')
response2 = eval(connection2.read())
print (response2['response']['numFound'], "documents found")
connection3 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Afriendli*&wt=python')
response3 = eval(connection3.read())
print (response3['response']['numFound'], "documents found")
connection4 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Ahooke*&wt=python')
response4 = eval(connection4.read())
print (response4['response']['numFound'], "documents found")
connection5 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Amemori*&wt=python')
response5 = eval(connection5.read())
print (response5['response']['numFound'], "documents found")
connection6 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Aclothin*&wt=python')
response6 = eval(connection6.read())
print (response6['response']['numFound'], "documents found")
connection7 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Aseasonal*&wt=python')
response7 = eval(connection7.read())
print (response7['response']['numFound'], "documents found")
connection8 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Atransp*&wt=python')
response8 = eval(connection8.read())
print (response8['response']['numFound'], "documents found")
connection9 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Abedroo*&wt=python')
response9 = eval(connection9.read())
print (response9['response']['numFound'], "documents found")
connection10 = urlopen('http://localhost:8983/solr/yelp_review500/select?q=review%3Askeptic*&wt=python')
response10 = eval(connection10.read())
print (response10['response']['numFound'], "documents found")

# end time
end_time = time.time()
count = (end_time - start_time)
msecs = (count * 1000)

# total time taken
print(f"Runtime of the query is {count:0.4f} seconds, or {msecs:0.2f} msec(s)")
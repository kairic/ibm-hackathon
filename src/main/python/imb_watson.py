from watson_developer_cloud import DiscoveryV1
import json

version="2018-03-05"
username="0013ab3f-5344-4203-91eb-1db0b958159f"
password = "tmqOrni8dUmu"
environment_id=  "system"
collection_id="news-en"

discovery = DiscoveryV1(
    version=version,
    username=username,
    password=password
)

query = 'baba'
filter = "language:(english|en),crawl_date>2018-03-08T12:00:00+0800,crawl_date<2018-05-08T12:00:00+0800"
aggregation = "term(host).term(enriched_text.sentiment.document.label)"

my_query = discovery.query(environment_id=environment_id, collection_id=collection_id, query='{query}', filter=filter, aggregations=[
    "term(host).term(enriched_text.sentiment.document.label)",
    "term(enriched_text.sentiment.document.label)"
])
print(json.dumps(my_query, indent=2))

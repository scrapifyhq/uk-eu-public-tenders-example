import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("scrapefy/public-tenders-scraper").call(run_input={
    "sources": ["ted", "findATender", "contractsFinder"],
    "keywords": ["software", "cloud hosting"],
    "noticeStage": "tenders",      # open tenders only; "awards" for who won
    "daysBack": 7,
    "maxItems": 100,               # per source
})

for n in client.dataset(run["defaultDatasetId"]).iterate_items():
    if n.get("type") == "error":
        print("source problem:", n)
        continue
    print(n["source"], n["publishedDate"][:10], n["buyerName"], n["valueAmount"], n["valueCurrency"], n["title"][:70])

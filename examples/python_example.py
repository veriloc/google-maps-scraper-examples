import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("h1018y/anvil-google-maps-scraper").call(
    run_input={
        "searchStringsArray": ["dentist"],
        "locationQuery": "Chicago, USA",
        "maxCrawledPlacesPerSearch": 30,
    }
)

for place in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(place.get("title"), "|", place.get("address"), "|", place.get("phone"), "|", place.get("totalScore"))

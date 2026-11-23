import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor("h1018y/anvil-google-maps-scraper").call({
  searchStringsArray: ["dentist"],
  locationQuery: "Chicago, USA",
  maxCrawledPlacesPerSearch: 30,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const place of items) {
  console.log(place.title, "|", place.address, "|", place.phone, "|", place.totalScore);
}

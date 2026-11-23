# Google Maps Scraper: code examples

Run the [Google Maps Scraper on Apify](https://apify.com/h1018y/anvil-google-maps-scraper) from Python or Node.js and get places back as rows: name, address, phone, website, rating and review count. It reads public Google Maps pages. No login, no cookies.

## Quick start

1. Create an Apify account and copy your API token from the Console settings.
2. Install the client: `pip install apify-client` (Python) or `npm install apify-client` (Node.js).
3. Run an example:

```bash
export APIFY_TOKEN=your_token_here
python examples/python_example.py
# or
node examples/node_example.mjs
```

Both examples search for 30 dentists in Chicago and print each place on one line.

## Input

| Field | What it does | Example |
|---|---|---|
| `searchStringsArray` | Search words, one search per word | `["dentist"]` |
| `locationQuery` | City or area to search in | `"Chicago, USA"` |
| `maxCrawledPlacesPerSearch` | Most places to return per search word | `30` |
| `placeMinimumStars` | Only places with at least this rating | `"four"` |

The Input tab on the Apify page lists every field. A saved input from compass/crawler-google-places works here too, because the field names match.

## What a row looks like

Two rows from a real run (a pizza search in New York):

```json
[
  {
    "title": "Joe's Pizza Broadway",
    "categoryName": "Pizza restaurant",
    "address": "1435 Broadway, New York, NY 10018",
    "phone": "(646) 559-4878",
    "website": "https://www.joespizzanyc.com/",
    "totalScore": 4.4,
    "reviewsCount": 27702,
    "city": "New York",
    "countryCode": "US"
  },
  {
    "title": "NY Pizza Suprema",
    "categoryName": "Pizza restaurant",
    "address": "413 8th Ave, New York, NY 10001",
    "phone": "(212) 594-8939",
    "website": "https://www.nypizzasuprema.com/",
    "totalScore": 4.6,
    "reviewsCount": 8908,
    "city": "New York",
    "countryCode": "US"
  }
]
```

The full row has more fields. See `sample_output.json` for the short version used above.

## Try it without code

These saved examples open on Apify with the input filled in:

- [Dentists in Chicago](https://apify.com/h1018y/anvil-google-maps-scraper/examples/dentists-in-chicago)
- [Sushi and ramen in London, 4 stars and up](https://apify.com/h1018y/anvil-google-maps-scraper/examples/sushi-and-ramen-in-london)

## Cost

You pay per result. The current price is on the Pricing tab of the Apify page, and Apify's free plan credit covers a test run.

## Limits

- Google shows a limited number of places per search, so split a large area into smaller searches.
- The tool reads only what a visitor sees without logging in.

## Problems and questions

Found a bug or a missing field? Open an issue on the [Apify page](https://apify.com/h1018y/anvil-google-maps-scraper) (Issues tab) or here on GitHub.

Code in this repository is MIT licensed.

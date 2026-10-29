# UK Find a Tender + Contracts Finder + EU TED notices: Python and JavaScript example

Runnable example code for a step-by-step tutorial (link added here when the post is live).

**Disclosure:** the Apify Actor(s) used here were built by the author of this repo. They are pay-per-event; the article lists the prices and what rival Actors charge.

Actor page(s): https://apify.com/scrapefy/public-tenders-scraper

## Run it

You need an Apify account and API token (the free tier is enough to try it). Never commit your token; use an environment variable.

```bash
export APIFY_TOKEN=your_token_here

# Python
pip install -r requirements.txt
python example.py

# or JavaScript (Node 18+)
npm install
npm start
```

Each script starts the Actor, waits for it to finish and prints the rows. Change `maxItems` first if you want to cap the cost of a test run (it is a hard cap).

## Files

- `example.py`: Python version (apify-client).
- `example.mjs`: JavaScript version (apify-client, ES modules).
- `sample-output.json`: real rows from a previous run of the Actor(s), so you can see the schema without running anything. Long text fields are truncated in some rows.

## Notes

- Only publicly visible data is collected. Use it in line with the source site's terms and data-protection law.
- Questions or a missing field: open an issue on the Actor's page in the Apify Store, with the run link.

License: MIT (the example code only).

import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('scrapefy/public-tenders-scraper').call({
    sources: ['ted', 'findATender', 'contractsFinder'],
    keywords: ['software', 'cloud hosting'],
    noticeStage: 'tenders',
    daysBack: 7,
    maxItems: 100,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const n of items.filter((x) => x.type !== 'error')) {
    console.log(n.source, n.buyerName, n.valueAmount, n.valueCurrency, n.title);
}

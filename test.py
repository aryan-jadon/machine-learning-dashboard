from news_articles import extract_rss_feeds

all_records = extract_rss_feeds("https://rss.nytimes.com/services/xml/rss/nyt/US.xml")
print(all_records)
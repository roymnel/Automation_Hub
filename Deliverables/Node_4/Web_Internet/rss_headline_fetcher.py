# RSS Feed Headline Fetcher
import feedparser

def fetch_rss_titles(feed_url):
    try:
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            print("❌ No entries found or invalid feed.")
            return
        print(f"\n📰 Latest headlines from: {feed.feed.title}")
        for entry in feed.entries[:5]:
            print(" -", entry.title)
    except Exception as e:
        print("❌ Error parsing feed:", e)

if __name__ == "__main__":
    url = input("Enter RSS feed URL: ").strip()
    fetch_rss_titles(url)

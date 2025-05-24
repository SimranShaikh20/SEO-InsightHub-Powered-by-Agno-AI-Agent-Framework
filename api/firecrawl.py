FIRECRAWL_API_KEY = "fc-5de4b54e2adf416bbc93b3803f6cab70"

def crawl_website(url):
    # TODO: Use FIRECRAWL_API_KEY in your request headers or params
    print(f"Using Firecrawl API Key: {FIRECRAWL_API_KEY}")
    return {
        "url": url,
        "title_tag": "Example Title | Business",
        "meta_description": "This is a sample meta description.",
        "headings": {
            "h1": 1,
            "h2": 3,
            "h3": 5
        },
        "images_with_alt": 12,
        "page_speed_score": 82
    }

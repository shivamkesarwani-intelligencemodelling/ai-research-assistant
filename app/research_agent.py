from search import search_web
from scraper import extract_text


def gather_research(topic, max_sources=3):
    results = search_web(topic, max_results=max_sources)

    sources = []

    for result in results:
        print(f"Reading: {result['title']}")

        content = extract_text(result["url"])

        if content:
            sources.append({
                "title": result["title"],
                "url": result["url"],
                "content": content[:5000]
            })

    return sources
#from dotenv import load_dotenv
from search import search_web

import os

#load_dotenv()


#api_key = os.getenv("OPENAI_API_KEY")

#if api_key:
#    print("API key loaded successfully")
#else:
#    print("API key not found")



#topic = input("Research topic: ")

#results = search_web(topic)

#print("\nSources Found:\n")

#for i, result in enumerate(results, start=1):
#    print(f"{i}. {result['title']}")
#    print(result['url'])
#    print()


#from search import search_web
#from scraper import extract_text

#topic = input("Research topic: ")

#results = search_web(topic)

#if results:
#    url = results[0]["url"]

#    print(f"\nReading:\n{url}\n")

#    text = extract_text(url)

#    print(text[:1500])



from research_agent import gather_research
from report_writer import generate_report

topic = input("Research topic: ")

print("\nSearching and collecting sources...\n")

sources = gather_research(topic)

print("\nGenerating report...\n")

report = generate_report(topic, sources)

filename = (
    topic.lower()
    .replace(" ", "_")
    .replace("/", "_")
)

path = f"reports/{filename}.md"

with open(path, "w", encoding="utf-8") as f:
    f.write(report)

print(f"\nReport saved to {path}")
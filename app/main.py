from dotenv import load_dotenv
from search import search_web

import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key loaded successfully")
else:
    print("API key not found")



topic = input("Research topic: ")

results = search_web(topic)

print("\nSources Found:\n")

for i, result in enumerate(results, start=1):
    print(f"{i}. {result['title']}")
    print(result['url'])
    print()
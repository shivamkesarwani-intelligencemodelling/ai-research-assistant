from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query, max_results=5):
    response = client.search(
        query=query,
        max_results=max_results
    )

    return response.get("results", [])
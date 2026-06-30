import requests
from bs4 import BeautifulSoup


def extract_text(url):
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:10000]

    except Exception as e:
        print(f"Error reading {url}: {e}")
        return ""
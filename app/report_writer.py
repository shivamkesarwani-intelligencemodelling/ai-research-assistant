from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_report(topic, sources):
    report = f"# {topic}\n\n"

    for source in sources:
        report += f"## {source['title']}\n"
        report += f"Source: {source['url']}\n\n"
        report += source['content'][:1000]
        report += "\n\n"

    return report
'''
def generate_report(topic, sources):

    source_text = ""

    for source in sources:
        source_text += f"""
TITLE: {source['title']}
URL: {source['url']}

CONTENT:
{source['content']}

--------------------
"""

    prompt = f"""
You are a professional research analyst.

Research Topic:
{topic}

Using the provided sources, create:

1. Executive Summary
2. Key Findings
3. Important Trends
4. Risks or Challenges
5. Conclusion

Include citations using source titles.
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": source_text
            }
        ]
    )

    return response.output_text
    '''
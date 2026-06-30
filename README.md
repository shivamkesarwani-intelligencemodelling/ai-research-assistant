# AI Research Assistant

A Python-based research assistant that automates the process of gathering information from the web and generating structured research reports.

The application searches for relevant sources, extracts content from webpages, and compiles findings into a Markdown report for further analysis. The project serves as a foundation for building more advanced AI-powered research systems, including retrieval-augmented generation (RAG), multi-agent workflows, and autonomous research assistants.

---

## Features

* Web search integration
* Automated source discovery
* Webpage content extraction
* Markdown report generation
* Research notes aggregation
* Command-line interface
* Modular architecture for future AI integration
* Extensible design for RAG and agent-based workflows

---

## Project Structure

```text
ai-research-assistant/
├── app/
│   ├── main.py
│   ├── research_agent.py
│   ├── search.py
│   ├── scraper.py
│   └── report_writer.py
│
├── reports/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

```text
User Query
    ↓
Web Search
    ↓
Collect Sources
    ↓
Extract Content
    ↓
Generate Report
    ↓
Save Markdown File
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

> OpenAI integration is optional. The current version can generate research reports without AI summarization.

---

## Usage

### Interactive Mode

```bash
python app/main.py
```

Example:

```text
Research topic:
Future of AI agents
```

### Command-Line Mode

```bash
python app/main.py "Future of AI agents"
```

---

## Output

Generated reports are stored in the `reports/` directory.

Example:

```text
reports/future_of_ai_agents.md
```

Each report contains:

* Research topic
* Generation timestamp
* Source list
* Extracted research notes
* Referenced URLs

---

## Example Use Cases

* Technology trend analysis
* Market research
* Competitive intelligence
* Industry reports
* Academic research assistance
* Literature review preparation
* Topic exploration and learning

---

## Why This Project?

As someone with experience in both academic research and machine learning engineering, I have spent significant time collecting information from papers, technical documentation, research articles, and online resources.

This project was created to automate key parts of the research workflow:

* Discover relevant information sources
* Extract and organize content
* Generate structured research notes
* Reduce time spent on manual information gathering
* Build a foundation for AI-powered research automation

The project serves as a practical exploration of information retrieval, research automation, and intelligent agent systems.

---

## Current Status

### Completed

* Web search functionality
* Source collection
* Web scraping
* Markdown report generation
* Report storage
* CLI workflow

### In Progress

* Improved source ranking
* Better report formatting
* Structured research notes

### Planned

* LLM-powered summarization
* Retrieval-Augmented Generation (RAG)
* Source credibility scoring
* PDF and research paper ingestion
* Research memory and persistence
* Multi-agent workflows
* Citation generation
* FastAPI backend
* Interactive web interface

---

## Future Vision

The current version focuses on source discovery and report generation.

Future versions will evolve into a comprehensive AI research copilot capable of:

* Planning research tasks
* Gathering information from multiple sources
* Fact-checking findings
* Producing structured reports
* Maintaining long-term research memory
* Supporting technical, academic, and business research workflows

The long-term architecture is expected to include specialized agents such as:

```text
Planner Agent
      ↓
Research Agent
      ↓
Fact Checker Agent
      ↓
Writer Agent
```

---

## Technologies Used

* Python 3.12+
* Requests
* BeautifulSoup4
* Python Dotenv
* Tavily Search API
* OpenAI API (optional)

---

## Related Experience

The ideas behind this project are influenced by experience in:

* Production-scale machine learning systems
* Natural language processing (NLP)
* Time-series forecasting
* Computer vision applications
* Deep learning research
* Scientific computing
* Information retrieval workflows

This project represents an intersection of machine learning engineering, research methodology, and AI-assisted knowledge discovery.

---

## Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## License

This project is licensed under the MIT License.

---

## About the Author

Shivam Kesarwani is a Machine Learning Engineer with experience building production-scale AI and machine learning systems across education technology and cloud optimization domains.

Areas of interest include:

* Artificial Intelligence
* Machine Learning
* Natural Language Processing
* Research Automation
* Intelligent Agents
* Scientific Computing

This repository is part of an ongoing effort to explore practical applications of AI systems for knowledge discovery, research assistance, and automated reasoning.

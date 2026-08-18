"""
AI-Assisted Research Summary Generator
---------------------------------------
Batch-processes a list of business/operations topics through the Claude API
and writes structured summaries (executive summary, key insights, recommended
workflow) to a timestamped CSV file for downstream reporting.

Usage:
    export ANTHROPIC_API_KEY="your-key-here"
    python claude_automation.py
    python claude_automation.py --topics topics.txt --output results.csv
"""

import argparse
import csv
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import anthropic

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

MODEL = "claude-sonnet-5"  # check docs.claude.com for the current recommended model string
MAX_TOKENS = 600

DEFAULT_TOPICS = [
    "Automating client onboarding via CRM and webhooks",
    "Reducing manual data entry in monthly reporting",
    "Standardizing async communication for remote teams",
]


def get_client() -> anthropic.Anthropic:
    """Create an Anthropic client, failing fast with a clear error if no key is set."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error(
            "ANTHROPIC_API_KEY is not set. Run: export ANTHROPIC_API_KEY='your-key-here'"
        )
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


def run_administrative_research(client: anthropic.Anthropic, topic: str) -> dict:
    """
    Sends a single topic to Claude and returns a structured operational
    breakdown. Returns a dict so results can be written straight to CSV.
    """
    prompt = f"""You are an AI Operations Assistant. Analyze the following topic
and provide a structured operational breakdown.

Topic: {topic}

Format requirements:
- Executive Summary (2-3 sentences)
- 3 Key Actionable Insights (numbered list)
- Recommended Process Workflow (numbered steps)
"""

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text
        return {"topic": topic, "status": "success", "summary": text}
    except anthropic.APIError as e:
        logger.warning("API error for topic %r: %s", topic, e)
        return {"topic": topic, "status": "error", "summary": str(e)}


def load_topics(path: str | None) -> list[str]:
    """Load topics from a text file (one per line), or fall back to defaults."""
    if not path:
        return DEFAULT_TOPICS
    topics_path = Path(path)
    if not topics_path.exists():
        logger.error("Topics file not found: %s", path)
        sys.exit(1)
    lines = [line.strip() for line in topics_path.read_text().splitlines()]
    return [line for line in lines if line]


def write_results_csv(results: list[dict], output_path: str) -> None:
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["topic", "status", "summary"])
        writer.writeheader()
        writer.writerows(results)
    logger.info("Wrote %d result(s) to %s", len(results), output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--topics", help="Path to a text file with one topic per line", default=None
    )
    parser.add_argument(
        "--output",
        help="Path to write the results CSV (default: results_<timestamp>.csv)",
        default=None,
    )
    args = parser.parse_args()

    topics = load_topics(args.topics)
    output_path = args.output or f"results_{datetime.now():%Y%m%d_%H%M%S}.csv"

    client = get_client()

    results = []
    for i, topic in enumerate(topics, start=1):
        logger.info("[%d/%d] Processing: %s", i, len(topics), topic)
        results.append(run_administrative_research(client, topic))

    write_results_csv(results, output_path)

    succeeded = sum(1 for r in results if r["status"] == "success")
    logger.info("Done: %d/%d topics processed successfully", succeeded, len(topics))


if __name__ == "__main__":
    main()

# AI Workflow Automation

> AI-driven operational solutions leveraging Python, SQL, and the Claude API platform.

## Project Overview

This repository contains automated workflows and scripts designed to optimize business operations, streamline research and drafting, and improve reporting efficiency. It bridges administrative management with AI-driven process automation.

A small Python script that batch-processes a list of business/operations topics through the Claude API and writes structured summaries (executive summary, key insights, recommended workflow) to a CSV file — built as a lightweight tool for turning a list of open questions into a first-pass research brief.

See [`sample_output.md`](sample_output.md) for an example of what the output looks like.

## What it does

- Reads a list of topics (one per line) from a text file.
- Sends each topic to Claude with a fixed prompt template asking for a structured operational breakdown.
- Writes all results — including any topics that failed — to a timestamped CSV file (`topic`, `status`, `summary`).
- Logs progress to the console as it works through the list.

## What it doesn't do (yet)

This is a small, single-purpose script, not a full pipeline. It doesn't currently: read from a live data source (CRM, spreadsheet, database), retry failed requests, or run on a schedule. Those are natural next steps — see [Ideas for extending](#ideas-for-extending) below.

## Setup

```bash
git clone [https://github.com/Marvellousblow/ai-workflow-automation.git](https://github.com/Marvellousblow/ai-workflow-automation.git)
cd ai-workflow-automation
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-api-key-here"

## Usage  

python claude_automation.py
python claude_automation.py --topics topics.txt --output results.csv

## Tech Stack & Tools

Languages: Python, SQL
AI Platform: Anthropic Claude API (Claude 101, Platform 101)
Data & Reporting: SQL Database Querying, Advanced Excel
Operations & Management: Process Automation, SOP Development, Prompt Engineering
Output: CSV, for easy import into Excel/Sheets or downstream reporting

## Ideas for Extending

Pull topics directly from a Google Sheet or Notion database instead of a text file.
Add retry logic with backoff for transient API errors.
Schedule as a recurring job (cron / GitHub Actions) for a standing research digest.
Parse the structured summary into separate CSV columns (summary / insights / workflow) instead of one text blob

## License

MIT — feel free to fork and adapt.
---
**Author:** Marvellous Gift Ighoyivwi  
**Role:** AI Operations & Business Support Specialist  
**Email:** imarvellousgift@gmail.com  
**Connect:** (https://linkedin.com/in/marvellous-ighoyivwi-3b45a8417)

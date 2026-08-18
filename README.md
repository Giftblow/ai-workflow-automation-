# AI-Assisted Research Summary Generator

A small Python script that batch-processes a list of business/operations
topics through the Claude API and writes structured summaries (executive
summary, key insights, recommended workflow) to a CSV file — built as a
lightweight tool for turning a list of open questions into a first-pass
research brief.

See [`sample_output.md`](sample_output.md) for an example of what the output
looks like.

## What it does

- Reads a list of topics (one per line) from a text file
- Sends each topic to Claude with a fixed prompt template asking for a
  structured operational breakdown
- Writes all results — including any topics that failed — to a timestamped
  CSV file (`topic`, `status`, `summary`)
- Logs progress to the console as it works through the list

## What it doesn't do (yet)

This is a small, single-purpose script, not a full pipeline. It doesn't
currently: read from a live data source (CRM, spreadsheet, database),
retry failed requests, or run on a schedule. Those are natural next steps —
see [Ideas for extending](#ideas-for-extending) below.

## Setup

```bash
git clone https://github.com/Marvellousblow/ai-workflow-automation-.git
cd ai-workflow-automation-
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

Run with the default sample topics:

```bash
python claude_automation.py
```

Run against your own list of topics and choose an output file:

```bash
python claude_automation.py --topics topics.txt --output results.csv
```

Each line of the topics file becomes one row in the output CSV.

## Tech stack

- **Language:** Python 3.10+
- **API:** [Anthropic Claude API](https://docs.claude.com) (`anthropic` Python SDK)
- **Output:** CSV, for easy import into Excel/Sheets or downstream reporting

## Ideas for extending

- Pull topics directly from a Google Sheet or Notion database instead of a text file
- Add retry logic with backoff for transient API errors
- Schedule as a recurring job (cron / GitHub Actions) for a standing research digest
- Parse the structured summary into separate CSV columns (summary / insights / workflow) instead of one text blob

## License

MIT — feel free to fork and adapt.

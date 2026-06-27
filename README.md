# Walmart Sales — Claude Code Demo

A practical demo of Claude Code features using the [Walmart Sales dataset](https://www.kaggle.com/datasets/mikhail1681/walmart-sales).

## What this repo demonstrates

| Feature | What it does |
|---|---|
| **CLAUDE.md** | Gives Claude persistent project context and coding conventions |
| **Agent Skills** | EDA skill Claude loads automatically when you ask to analyze data |
| **MCP (SQLite)** | Claude queries the sales database in natural language |
| **Subagents** | A custom `insight-writer` agent that writes business narratives |
| **Hooks** | A PreToolUse hook that blocks accidental deletion of the database |

## Setup

**Requirements:** Python 3.11+

```bash
# 1. Clone the repo
git clone <repo-url>
cd walmart-sales-demo

# 2. Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Place the Walmart CSV in data/
#    Download from: https://www.kaggle.com/datasets/mikhail1681/walmart-sales
#    Then: mv Walmart_Sales.csv data/

# 5. Create the SQLite database
python setup.py

# 6. Open Claude Code
claude
```

## MCP (SQLite)

The SQLite MCP server is configured in `.mcp.json` at the project root. It starts automatically when you open Claude Code **after** the `.venv` has been set up and `python setup.py` has been run — the server binary lives inside `.venv/Scripts/`.

The first time you open Claude Code in this project, you may be prompted to approve the MCP server defined in `.mcp.json`. Accept it.

To verify it's connected, run inside Claude Code:

```
/mcp
```

You should see `sqlite` listed as a connected server. If it shows nothing, re-run the setup steps and restart Claude Code. Claude can then query the database directly. Example prompts:

- *"Which store had the highest total sales?"*
- *"How did holiday weeks affect average weekly sales?"*
- *"Show me the top 5 weeks by sales across all stores."*

## Dataset

Historical weekly sales for 45 Walmart stores (2010–2012).

| Column | Description |
|---|---|
| `Store` | Store number (1–45) |
| `Date` | Week start date |
| `Weekly_Sales` | Total sales for the week |
| `Holiday_Flag` | 1 if holiday week, 0 otherwise |
| `Temperature` | Average temperature (°F) |
| `Fuel_Price` | Regional fuel price |
| `CPI` | Consumer Price Index |
| `Unemployment` | Regional unemployment rate |

## Repo structure

```
├── CLAUDE.md                        # Project context for Claude
├── setup.py                         # Creates SQLite DB from CSV
├── data/
│   ├── Walmart_Sales.csv            # Raw dataset (from Kaggle)
│   └── walmart.db                   # SQLite database (generated)
├── output/                          # Generated plots and reports
├── .mcp.json                        # MCP server config (project-scoped)
└── .claude/
    ├── settings.json                # Hooks config
    ├── agents/
    │   └── insight-writer.md        # Custom subagent definition
    ├── skills/
    │   └── eda/SKILL.md             # EDA skill definition
    └── hooks/
        └── protect_db.py            # Hook: blocks DB deletion
```

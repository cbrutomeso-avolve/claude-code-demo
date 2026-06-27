# Walmart Sales Analysis — Claude Code Demo

## Project
Retail sales analysis using Walmart's historical weekly sales data across 45 stores.
The goal is to uncover patterns in sales performance, seasonality, and the impact of external factors.

## Dataset
- Raw CSV: `data/Walmart_Sales.csv`
- Database: `data/walmart.db` (SQLite — **do not delete**)
- Columns: `Store`, `Date`, `Weekly_Sales`, `Holiday_Flag`, `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`

## Coding Conventions
- Always use Python with `pandas` and `matplotlib` / `seaborn`
- Save every generated plot to the `output/` directory
- Use snake_case for all variables and function names
- Keep code modular: one function per task
- Explain findings in plain English suitable for a non-technical business audience

## Output
- Plots → `output/*.png`
- Reports → `output/*.md`

## Important
Never delete `data/walmart.db`. Run `setup.py` to recreate it from the CSV if needed.

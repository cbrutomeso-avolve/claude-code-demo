---
name: eda
description: Use this skill when the user asks to explore, analyze, understand, or get an overview of a dataset. Triggers on requests like "analyze the data", "explore the dataset", "what does the data look like", "run an EDA", or "give me a summary of the data".
---

# Exploratory Data Analysis

When performing EDA, follow these steps in order:

## 1. Load and Inspect
- Load the dataset with pandas
- Print shape, column names, dtypes, and the first 5 rows

## 2. Data Quality
- Count missing values per column
- Check for duplicate rows
- Flag any columns with type mismatches (e.g. dates stored as strings)

## 3. Descriptive Statistics
- Run `.describe()` on all numerical columns
- Highlight the columns with the highest variance and the rows with min/max values

Create the `output/eda/` directory if it does not exist before saving any file.
Save all text output (inspection, data quality, statistics) to `output/eda/report.md` as a structured Markdown report. Append each section to the same file as you go.
Write all analysis code to `output/eda/eda.py` as a single self-contained script that can be re-run independently.

## 4. Distributions
- Plot histograms for all numerical columns
- Save to `output/eda/distributions.png`

## 5. Trends Over Time
- If a date column exists, plot the main metric over time
- If a categorical grouping column exists, use it to color or facet the plot
- Save to `output/eda/trends.png`

## 6. Group Comparison
- If a categorical column exists, compare the main metric across groups (bar chart)
- Save to `output/eda/group_comparison.png`

## 7. Correlation
- Heatmap of correlations between all numerical columns
- Save to `output/eda/correlation_heatmap.png`

## 8. Summary
Print 4-5 key observations in plain English.

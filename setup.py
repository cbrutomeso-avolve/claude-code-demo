import pandas as pd
import sqlite3
from pathlib import Path

CSV_PATH = Path("data/Walmart_Sales.csv")
DB_PATH = Path("data/walmart.db")


def setup():
    if not CSV_PATH.exists():
        print(f"Error: {CSV_PATH} not found.")
        print("Download it from: https://www.kaggle.com/datasets/mikhail1681/walmart-sales")
        return

    df = pd.read_csv(CSV_PATH)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("walmart_sales", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Database ready: {DB_PATH}")
    print(f"  Rows:    {len(df):,}")
    print(f"  Columns: {list(df.columns)}")


if __name__ == "__main__":
    setup()

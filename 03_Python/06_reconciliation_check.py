import pandas as pd
from pathlib import Path


# ============================================================
# DATA RECONCILIATION CHECK
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW = PROJECT_ROOT / "01_Raw_Data"
CLEANED = PROJECT_ROOT / "02_Cleaned_Data"


checks = [
    (
        "Instagram",
        RAW / "Instagram_Data.csv",
        CLEANED / "instagram_cleaned.csv"
    ),
    (
        "Twitter Sentiment",
        RAW / "Twitter_Data (2).csv",
        CLEANED / "twitter_sentiment_cleaned.csv"
    ),
    (
        "Twitter Category",
        RAW / "Twitter_Data.csv",
        CLEANED / "twitter_category_cleaned.csv"
    ),
    (
        "YouTube Comments",
        RAW / "Youtube_Data1.csv",
        CLEANED / "youtube_comments_cleaned.csv"
    ),
    (
        "YouTube Videos",
        RAW / "Youtube_Data2.csv",
        CLEANED / "youtube_videos_cleaned.csv"
    ),
]


print("\n" + "=" * 75)
print("             DATA ROW RECONCILIATION")
print("=" * 75)


results = []


for name, raw_file, cleaned_file in checks:

    raw_df = pd.read_csv(raw_file)
    cleaned_df = pd.read_csv(cleaned_file)

    raw_rows = len(raw_df)
    cleaned_rows = len(cleaned_df)

    removed = raw_rows - cleaned_rows

    percentage_removed = (
        removed / raw_rows * 100
        if raw_rows > 0
        else 0
    )

    results.append({
        "dataset": name,
        "raw_rows": raw_rows,
        "cleaned_rows": cleaned_rows,
        "rows_removed": removed,
        "percent_removed": round(
            percentage_removed,
            4
        )
    })


reconciliation = pd.DataFrame(results)


print(
    reconciliation.to_string(index=False)
)


# ============================================================
# SAVE RESULT
# ============================================================

OUTPUT = PROJECT_ROOT / "09_Analysis_Output"

OUTPUT.mkdir(
    exist_ok=True
)

output_file = OUTPUT / "data_reconciliation.csv"

reconciliation.to_csv(
    output_file,
    index=False
)

print("\nSaved:")
print(output_file)


print("\n" + "=" * 75)
print("             RECONCILIATION COMPLETE")
print("=" * 75)
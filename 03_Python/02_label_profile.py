import pandas as pd
from pathlib import Path


# ============================================================
# SOCIAL MEDIA ANALYSIS PROJECT
# LABEL AND CATEGORY PROFILE
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT_ROOT / "01_Raw_Data"


def profile_column(dataset_name, file_name, column_name):

    file_path = RAW_DATA / file_name

    print("\n" + "=" * 75)
    print(f"DATASET: {dataset_name}")
    print(f"COLUMN: {column_name}")
    print("=" * 75)

    df = pd.read_csv(file_path)

    print("\nVALUE COUNTS:")

    print(
        df[column_name]
        .value_counts(dropna=False)
        .to_string()
    )

    print("\nUNIQUE VALUES:")

    values = df[column_name].drop_duplicates().tolist()

    for value in values:
        print(f"  {repr(value)}")


# ============================================================
# PROFILE ALL IMPORTANT LABEL/CATEGORY COLUMNS
# ============================================================

profile_column(
    "Instagram",
    "Instagram_Data.csv",
    "sentiment_label_rater1"
)

profile_column(
    "Instagram Category",
    "Instagram_Data.csv",
    "category"
)

profile_column(
    "Twitter Sentiment",
    "Twitter_Data (2).csv",
    "sentiment"
)

profile_column(
    "Twitter Category",
    "Twitter_Data.csv",
    "category"
)

profile_column(
    "YouTube Nostalgia",
    "Youtube_Data1.csv",
    "sentiment"
)

profile_column(
    "YouTube Video Category",
    "Youtube_Data2.csv",
    "category"
)


print("\n")
print("#" * 75)
print("                 LABEL PROFILE COMPLETE")
print("#" * 75)
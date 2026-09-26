import pandas as pd
from pathlib import Path


# ============================================================
# SOCIAL MEDIA ANALYSIS PROJECT
# CLEANED DATA VALIDATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CLEANED_DATA = PROJECT_ROOT / "02_Cleaned_Data"


datasets = {
    "Instagram": "instagram_cleaned.csv",
    "Twitter Sentiment": "twitter_sentiment_cleaned.csv",
    "Twitter Category": "twitter_category_cleaned.csv",
    "YouTube Comments": "youtube_comments_cleaned.csv",
    "YouTube Videos": "youtube_videos_cleaned.csv",
}


def validate_dataset(name, filename):

    print("\n" + "=" * 75)
    print(f"VALIDATING: {name}")
    print("=" * 75)

    file_path = CLEANED_DATA / filename

    # Check file
    if not file_path.exists():
        print("ERROR: Cleaned file not found.")
        print(f"Expected: {file_path}")
        return

    # Read file
    df = pd.read_csv(file_path)

    print(f"\nFile: {filename}")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    # --------------------------------------------------------
    # Missing values
    # --------------------------------------------------------

    print("\nMISSING VALUES:")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("  None")
    else:
        for column, count in missing.items():
            percentage = (count / len(df)) * 100
            print(
                f"  {column}: "
                f"{count:,} "
                f"({percentage:.2f}%)"
            )

    # --------------------------------------------------------
    # Duplicate rows
    # --------------------------------------------------------

    duplicates = df.duplicated().sum()

    print("\nDUPLICATE ROWS:")
    print(f"  {duplicates:,}")

    # --------------------------------------------------------
    # Column names
    # --------------------------------------------------------

    print("\nCOLUMNS:")

    for column in df.columns:
        print(f"  - {column}")

    # --------------------------------------------------------
    # Data types
    # --------------------------------------------------------

    print("\nDATA TYPES:")
    print(df.dtypes)

    # --------------------------------------------------------
    # Dataset-specific checks
    # --------------------------------------------------------

    if name == "Twitter Category":

        print("\nTWITTER SENTIMENT LABEL CHECK:")

        print(
            df["sentiment_label"]
            .value_counts(dropna=False)
            .to_string()
        )

    if name == "YouTube Comments":

        print("\nYOUTUBE NOSTALGIA LABEL CHECK:")

        print(
            df["sentiment"]
            .value_counts(dropna=False)
            .to_string()
        )

    if name == "YouTube Videos":

        print("\nYOUTUBE VIDEO ID CHECK:")

        print(
            df["id_valid"]
            .value_counts(dropna=False)
            .to_string()
        )

        print("\nYOUTUBE CATEGORY COUNTS:")

        print(
            df["category"]
            .value_counts()
            .to_string()
        )


# ============================================================
# RUN VALIDATION
# ============================================================

print("\n")
print("#" * 75)
print("        SOCIAL MEDIA ANALYSIS - CLEANED DATA VALIDATION")
print("#" * 75)

print(f"\nCleaned data folder:")
print(CLEANED_DATA)


for dataset_name, filename in datasets.items():

    validate_dataset(
        dataset_name,
        filename
    )


print("\n")
print("#" * 75)
print("                 VALIDATION COMPLETE")
print("#" * 75)
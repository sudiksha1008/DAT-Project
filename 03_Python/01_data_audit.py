import pandas as pd
from pathlib import Path


# ============================================================
# SOCIAL MEDIA ANALYSIS PROJECT
# DATA AUDIT SCRIPT
# ============================================================

# Project folders
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT_ROOT / "01_Raw_Data"


# ============================================================
# LOCKED DATASET LIST
# ============================================================

datasets = {
    "Instagram": RAW_DATA / "Instagram_Data.csv",

    "Twitter Sentiment": RAW_DATA / "Twitter_Data (2).csv",

    "Twitter Category": RAW_DATA / "Twitter_Data.csv",

    "YouTube Comments": RAW_DATA / "Youtube_Data1.csv",

    "YouTube Videos": RAW_DATA / "Youtube_Data2.csv",
}

# ============================================================
# DATASET AUDIT FUNCTION
# ============================================================

def audit_dataset(name, file_path):

    print("\n" + "=" * 75)
    print(f"DATASET: {name}")
    print("=" * 75)

    # Check whether file exists
    if not file_path.exists():
        print("\nERROR: File not found.")
        print(f"Expected location: {file_path}")
        return

    # Read CSV
    try:
        df = pd.read_csv(file_path)
    except Exception as error:
        print("\nERROR while reading file:")
        print(error)
        return

    # Basic information
    print(f"\nFile: {file_path.name}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")

    # Columns
    print("\nCOLUMNS:")
    for column in df.columns:
        print(f"  - {column}")

    # Data types
    print("\nDATA TYPES:")
    print(df.dtypes)

    # Missing values
    print("\nMISSING VALUES:")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("  No missing values.")
    else:
        for column, count in missing.items():
            percentage = (count / len(df)) * 100

            print(
                f"  {column}: "
                f"{count:,} "
                f"({percentage:.2f}%)"
            )

    # Duplicate rows
    duplicates = df.duplicated().sum()

    print("\nDUPLICATE ROWS:")
    print(f"  {duplicates:,}")

    # First three records
    print("\nFIRST 3 RECORDS:")

    print(
        df.head(3).to_string(index=False)
    )


# ============================================================
# START AUDIT
# ============================================================

print("\n")
print("#" * 75)
print("        SOCIAL MEDIA ANALYSIS - DATA AUDIT")
print("#" * 75)

print("\nProject folder:")
print(PROJECT_ROOT)

print("\nRaw data folder:")
print(RAW_DATA)


# Run audit for every dataset
for dataset_name, dataset_path in datasets.items():

    audit_dataset(
        dataset_name,
        dataset_path
    )


# ============================================================
# END
# ============================================================

print("\n")
print("#" * 75)
print("                    AUDIT COMPLETE")
print("#" * 75)
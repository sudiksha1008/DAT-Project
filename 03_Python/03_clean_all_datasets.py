import pandas as pd
from pathlib import Path


# ============================================================
# SOCIAL MEDIA ANALYSIS PROJECT
# CLEANING PIPELINE
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "01_Raw_Data"
CLEANED_DATA = PROJECT_ROOT / "02_Cleaned_Data"

# Create cleaned-data folder if it does not exist
CLEANED_DATA.mkdir(exist_ok=True)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def clean_text_column(df, column):
    """Standardize text while preserving the original meaning."""

    df[column] = df[column].astype("string")

    df[column] = (
        df[column]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    return df


def save_dataset(df, filename):
    """Save cleaned dataset."""

    output_path = CLEANED_DATA / filename
    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print()


# ============================================================
# 1. INSTAGRAM
# ============================================================

print("\n" + "=" * 75)
print("CLEANING: INSTAGRAM")
print("=" * 75)

instagram = pd.read_csv(
    RAW_DATA / "Instagram_Data.csv"
)

# Remove exact duplicate rows
instagram = instagram.drop_duplicates().copy()

# Convert date column
instagram["created_at"] = pd.to_datetime(
    instagram["created_at"],
    errors="coerce"
)

# Clean text
instagram = clean_text_column(
    instagram,
    "text"
)

# Ensure likes are numeric
instagram["likes"] = pd.to_numeric(
    instagram["likes"],
    errors="coerce"
)

# Remove unnecessary identifying fields
instagram_analysis = instagram.drop(
    columns=["user_id", "username"],
    errors="ignore"
)

save_dataset(
    instagram_analysis,
    "instagram_cleaned.csv"
)


# ============================================================
# 2. TWITTER SENTIMENT
# ============================================================

print("\n" + "=" * 75)
print("CLEANING: TWITTER SENTIMENT")
print("=" * 75)

twitter_sentiment = pd.read_csv(
    RAW_DATA / "Twitter_Data (2).csv"
)

# Remove exact duplicate rows
twitter_sentiment = (
    twitter_sentiment
    .drop_duplicates()
    .copy()
)

# Clean text
twitter_sentiment = clean_text_column(
    twitter_sentiment,
    "text"
)

# Keep original binary label
twitter_sentiment["sentiment"] = pd.to_numeric(
    twitter_sentiment["sentiment"],
    errors="coerce"
)

save_dataset(
    twitter_sentiment,
    "twitter_sentiment_cleaned.csv"
)


# ============================================================
# 3. TWITTER CATEGORY / SENTIMENT
# ============================================================

print("\n" + "=" * 75)
print("CLEANING: TWITTER CATEGORY")
print("=" * 75)

twitter_category = pd.read_csv(
    RAW_DATA / "Twitter_Data.csv"
)

# Remove exact duplicates
twitter_category = (
    twitter_category
    .drop_duplicates()
    .copy()
)

# Clean text
twitter_category = clean_text_column(
    twitter_category,
    "clean_text"
)

# Convert category to numeric
twitter_category["category"] = pd.to_numeric(
    twitter_category["category"],
    errors="coerce"
)

# Remove rows where either text or category is missing
twitter_category = twitter_category.dropna(
    subset=["clean_text", "category"]
).copy()

# Map documented sentiment labels
twitter_category["sentiment_label"] = (
    twitter_category["category"]
    .map({
        -1: "negative",
         0: "neutral",
         1: "positive"
    })
)

save_dataset(
    twitter_category,
    "twitter_category_cleaned.csv"
)


# ============================================================
# 4. YOUTUBE COMMENTS
# ============================================================

print("\n" + "=" * 75)
print("CLEANING: YOUTUBE COMMENTS")
print("=" * 75)

youtube_comments = pd.read_csv(
    RAW_DATA / "Youtube_Data1.csv"
)

# Remove exact duplicates
youtube_comments = (
    youtube_comments
    .drop_duplicates()
    .copy()
)

# Clean comment text
youtube_comments = clean_text_column(
    youtube_comments,
    "comment"
)

# Standardize sentiment labels
youtube_comments["sentiment"] = (
    youtube_comments["sentiment"]
    .astype("string")
    .str.strip()
    .str.lower()
)

save_dataset(
    youtube_comments,
    "youtube_comments_cleaned.csv"
)


# ============================================================
# 5. YOUTUBE VIDEOS
# ============================================================

print("\n" + "=" * 75)
print("CLEANING: YOUTUBE VIDEOS")
print("=" * 75)

youtube_videos = pd.read_csv(
    RAW_DATA / "Youtube_Data2.csv"
)

# Remove exact duplicates
youtube_videos = (
    youtube_videos
    .drop_duplicates()
    .copy()
)

# Convert date
youtube_videos["upload_date"] = pd.to_datetime(
    youtube_videos["upload_date"].astype("string"),
    format="%Y%m%d",
    errors="coerce"
)

# Numeric columns
numeric_columns = [
    "duration_s",
    "width",
    "height",
    "fps",
    "view_count",
    "like_count"
]

for column in numeric_columns:

    youtube_videos[column] = pd.to_numeric(
        youtube_videos[column],
        errors="coerce"
    )

# Clean title
youtube_videos = clean_text_column(
    youtube_videos,
    "title"
)

# The license column is 100% missing,
# so it is removed from the analytical dataset.
youtube_videos = youtube_videos.drop(
    columns=["license"],
    errors="ignore"
)

# Flag invalid/malformed IDs rather than silently deleting them.
youtube_videos["id_valid"] = (
    youtube_videos["id"].astype("string").str.match(
        r"^[A-Za-z0-9_-]{11}$",
        na=False
    )
)

save_dataset(
    youtube_videos,
    "youtube_videos_cleaned.csv"
)


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n" + "#" * 75)
print("             CLEANING PIPELINE COMPLETE")
print("#" * 75)

print("\nCleaned datasets were saved in:")

print(CLEANED_DATA)

print("\nRAW DATA WAS NOT MODIFIED.")
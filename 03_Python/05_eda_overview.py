import pandas as pd
import numpy as np
from pathlib import Path


# ============================================================
# SOCIAL MEDIA ANALYSIS PROJECT
# EXPLORATORY DATA ANALYSIS - OVERVIEW
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEANED_DATA = PROJECT_ROOT / "02_Cleaned_Data"
OUTPUT = PROJECT_ROOT / "09_Analysis_Output"

OUTPUT.mkdir(exist_ok=True)


# ============================================================
# HELPER FUNCTION
# ============================================================

def save_csv(df, filename):
    path = OUTPUT / filename
    df.to_csv(path, index=False)
    print(f"Saved: {path}")


# ============================================================
# LOAD CLEANED DATA
# ============================================================

print("\n" + "#" * 75)
print("       SOCIAL MEDIA ANALYSIS - EXPLORATORY DATA ANALYSIS")
print("#" * 75)


instagram = pd.read_csv(
    CLEANED_DATA / "instagram_cleaned.csv"
)

twitter_sentiment = pd.read_csv(
    CLEANED_DATA / "twitter_sentiment_cleaned.csv"
)

twitter_category = pd.read_csv(
    CLEANED_DATA / "twitter_category_cleaned.csv"
)

youtube_comments = pd.read_csv(
    CLEANED_DATA / "youtube_comments_cleaned.csv"
)

youtube_videos = pd.read_csv(
    CLEANED_DATA / "youtube_videos_cleaned.csv"
)


# ============================================================
# 1. DATASET SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("1. DATASET SUMMARY")
print("=" * 75)

dataset_summary = pd.DataFrame({
    "dataset": [
        "Instagram",
        "Twitter Sentiment",
        "Twitter Category",
        "YouTube Comments",
        "YouTube Videos"
    ],
    "rows": [
        len(instagram),
        len(twitter_sentiment),
        len(twitter_category),
        len(youtube_comments),
        len(youtube_videos)
    ],
    "columns": [
        len(instagram.columns),
        len(twitter_sentiment.columns),
        len(twitter_category.columns),
        len(youtube_comments.columns),
        len(youtube_videos.columns)
    ]
})

print(dataset_summary.to_string(index=False))

save_csv(
    dataset_summary,
    "dataset_summary.csv"
)


# ============================================================
# 2. INSTAGRAM SENTIMENT DISTRIBUTION
# ============================================================

print("\n" + "=" * 75)
print("2. INSTAGRAM SENTIMENT DISTRIBUTION")
print("=" * 75)

instagram_sentiment = (
    instagram["sentiment_label_rater1"]
    .value_counts()
    .reset_index()
)

instagram_sentiment.columns = [
    "sentiment",
    "count"
]

instagram_sentiment["percentage"] = (
    instagram_sentiment["count"]
    / instagram_sentiment["count"].sum()
    * 100
)

print(
    instagram_sentiment.to_string(index=False)
)

save_csv(
    instagram_sentiment,
    "instagram_sentiment_distribution.csv"
)


# ============================================================
# 3. INSTAGRAM CATEGORY DISTRIBUTION
# ============================================================

print("\n" + "=" * 75)
print("3. INSTAGRAM CATEGORY DISTRIBUTION")
print("=" * 75)

instagram_category = (
    instagram["category"]
    .value_counts()
    .reset_index()
)

instagram_category.columns = [
    "category",
    "count"
]

instagram_category["percentage"] = (
    instagram_category["count"]
    / instagram_category["count"].sum()
    * 100
)

print(
    instagram_category.to_string(index=False)
)

save_csv(
    instagram_category,
    "instagram_category_distribution.csv"
)


# ============================================================
# 4. INSTAGRAM SENTIMENT BY CATEGORY
# ============================================================

print("\n" + "=" * 75)
print("4. INSTAGRAM SENTIMENT BY CATEGORY")
print("=" * 75)

instagram_cross = pd.crosstab(
    instagram["category"],
    instagram["sentiment_label_rater1"]
)

print(
    instagram_cross.to_string()
)

instagram_cross.to_csv(
    OUTPUT / "instagram_sentiment_by_category.csv"
)

print(
    f"Saved: {OUTPUT / 'instagram_sentiment_by_category.csv'}"
)


# ============================================================
# 5. TWITTER BINARY SENTIMENT DISTRIBUTION
# ============================================================

print("\n" + "=" * 75)
print("5. TWITTER BINARY SENTIMENT DISTRIBUTION")
print("=" * 75)

twitter_binary = (
    twitter_sentiment["sentiment"]
    .value_counts()
    .sort_index()
    .reset_index()
)

twitter_binary.columns = [
    "sentiment_code",
    "count"
]

twitter_binary["percentage"] = (
    twitter_binary["count"]
    / twitter_binary["count"].sum()
    * 100
)

print(
    twitter_binary.to_string(index=False)
)

save_csv(
    twitter_binary,
    "twitter_binary_sentiment_distribution.csv"
)


# ============================================================
# 6. TWITTER THREE-CLASS SENTIMENT
# ============================================================

print("\n" + "=" * 75)
print("6. TWITTER THREE-CLASS SENTIMENT")
print("=" * 75)

twitter_three_class = (
    twitter_category["sentiment_label"]
    .value_counts()
    .reindex(
        ["negative", "neutral", "positive"],
        fill_value=0
    )
    .reset_index()
)

twitter_three_class.columns = [
    "sentiment",
    "count"
]

twitter_three_class["percentage"] = (
    twitter_three_class["count"]
    / twitter_three_class["count"].sum()
    * 100
)

print(
    twitter_three_class.to_string(index=False)
)

save_csv(
    twitter_three_class,
    "twitter_three_class_sentiment_distribution.csv"
)


# ============================================================
# 7. YOUTUBE NOSTALGIA DISTRIBUTION
# ============================================================

print("\n" + "=" * 75)
print("7. YOUTUBE NOSTALGIA DISTRIBUTION")
print("=" * 75)

youtube_nostalgia = (
    youtube_comments["sentiment"]
    .value_counts()
    .reset_index()
)

youtube_nostalgia.columns = [
    "classification",
    "count"
]

youtube_nostalgia["percentage"] = (
    youtube_nostalgia["count"]
    / youtube_nostalgia["count"].sum()
    * 100
)

print(
    youtube_nostalgia.to_string(index=False)
)

save_csv(
    youtube_nostalgia,
    "youtube_nostalgia_distribution.csv"
)


# ============================================================
# 8. YOUTUBE VIDEO CATEGORY DISTRIBUTION
# ============================================================

print("\n" + "=" * 75)
print("8. YOUTUBE VIDEO CATEGORY DISTRIBUTION")
print("=" * 75)

youtube_category = (
    youtube_videos["category"]
    .value_counts()
    .reset_index()
)

youtube_category.columns = [
    "category",
    "video_count"
]

youtube_category["percentage"] = (
    youtube_category["video_count"]
    / youtube_category["video_count"].sum()
    * 100
)

print(
    youtube_category.to_string(index=False)
)

save_csv(
    youtube_category,
    "youtube_video_category_distribution.csv"
)


# ============================================================
# 9. YOUTUBE ENGAGEMENT SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("9. YOUTUBE ENGAGEMENT SUMMARY")
print("=" * 75)

engagement_columns = [
    "view_count",
    "like_count",
    "duration_s"
]

youtube_engagement = (
    youtube_videos[engagement_columns]
    .describe()
    .T
    .reset_index()
)

youtube_engagement.columns = [
    "metric",
    "count",
    "mean",
    "std",
    "min",
    "25_percentile",
    "median",
    "75_percentile",
    "max"
]

print(
    youtube_engagement.to_string(index=False)
)

save_csv(
    youtube_engagement,
    "youtube_engagement_summary.csv"
)


# ============================================================
# 10. YOUTUBE ENGAGEMENT BY CATEGORY
# ============================================================

print("\n" + "=" * 75)
print("10. YOUTUBE ENGAGEMENT BY CATEGORY")
print("=" * 75)

youtube_category_engagement = (
    youtube_videos
    .groupby("category")
    .agg(
        video_count=("id", "count"),
        total_views=("view_count", "sum"),
        average_views=("view_count", "mean"),
        median_views=("view_count", "median"),
        total_likes=("like_count", "sum"),
        average_likes=("like_count", "mean"),
        median_likes=("like_count", "median")
    )
    .reset_index()
    .sort_values(
        "average_views",
        ascending=False
    )
)

print(
    youtube_category_engagement.to_string(index=False)
)

save_csv(
    youtube_category_engagement,
    "youtube_engagement_by_category.csv"
)


# ============================================================
# 11. YOUTUBE VIEW-LIKE CORRELATION
# ============================================================

print("\n" + "=" * 75)
print("11. YOUTUBE VIEW-LIKE CORRELATION")
print("=" * 75)

correlation_data = youtube_videos[
    ["view_count", "like_count"]
].dropna()

correlation = correlation_data.corr(
    method="pearson"
)

print(correlation)

correlation.to_csv(
    OUTPUT / "youtube_view_like_correlation.csv"
)

print(
    f"Saved: {OUTPUT / 'youtube_view_like_correlation.csv'}"
)


# ============================================================
# 12. YOUTUBE LIKE RATE
# ============================================================

print("\n" + "=" * 75)
print("12. YOUTUBE LIKE RATE")
print("=" * 75)

youtube_videos["like_rate_percent"] = np.where(
    youtube_videos["view_count"] > 0,
    youtube_videos["like_count"]
    / youtube_videos["view_count"]
    * 100,
    np.nan
)

like_rate_summary = (
    youtube_videos[
        ["category", "like_rate_percent"]
    ]
    .groupby("category")
    .agg(
        average_like_rate=("like_rate_percent", "mean"),
        median_like_rate=("like_rate_percent", "median")
    )
    .reset_index()
    .sort_values(
        "average_like_rate",
        ascending=False
    )
)

print(
    like_rate_summary.to_string(index=False)
)

save_csv(
    like_rate_summary,
    "youtube_like_rate_by_category.csv"
)


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "#" * 75)
print("                 EDA OVERVIEW COMPLETE")
print("#" * 75)

print("\nAll analysis files were saved to:")

print(OUTPUT)
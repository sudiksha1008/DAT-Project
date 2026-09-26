import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# SOCIAL MEDIA ANALYSIS
# VISUALIZATION STAGE
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEANED = PROJECT_ROOT / "02_Cleaned_Data"
OUTPUT = PROJECT_ROOT / "09_Analysis_Output"

OUTPUT.mkdir(exist_ok=True)


def save_chart(filename):
    """
    Save the current matplotlib figure.
    """
    plt.tight_layout()
    plt.savefig(
        OUTPUT / filename,
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()


def bar_chart(series, title, xlabel, ylabel, filename, rotation=0):
    """
    Create and save a standard bar chart.
    """
    plt.figure(figsize=(10, 6))

    series.plot(kind="bar")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if rotation:
        plt.xticks(rotation=rotation)

    save_chart(filename)


# ============================================================
# LOAD CLEANED DATA
# ============================================================

instagram = pd.read_csv(
    CLEANED / "instagram_cleaned.csv"
)

twitter_sentiment = pd.read_csv(
    CLEANED / "twitter_sentiment_cleaned.csv"
)

twitter_category = pd.read_csv(
    CLEANED / "twitter_category_cleaned.csv"
)

youtube_comments = pd.read_csv(
    CLEANED / "youtube_comments_cleaned.csv"
)

youtube_videos = pd.read_csv(
    CLEANED / "youtube_videos_cleaned.csv"
)


print("\n" + "=" * 75)
print("              VISUALIZATION GENERATION")
print("=" * 75)


# ============================================================
# 1. INSTAGRAM SENTIMENT DISTRIBUTION
# ============================================================

instagram_sentiment = (
    instagram["sentiment_label_rater1"]
    .value_counts()
    .reindex(
        ["positive", "neutral", "negative"],
        fill_value=0
    )
)

bar_chart(
    instagram_sentiment,
    "Instagram Sentiment Distribution",
    "Sentiment",
    "Number of Comments",
    "instagram_sentiment_distribution.png"
)

print("Created: instagram_sentiment_distribution.png")


# ============================================================
# 2. INSTAGRAM CATEGORY DISTRIBUTION
# ============================================================

instagram_category = (
    instagram["category"]
    .value_counts()
)

bar_chart(
    instagram_category,
    "Instagram Content Category Distribution",
    "Category",
    "Number of Comments",
    "instagram_category_distribution.png"
)

print("Created: instagram_category_distribution.png")


# ============================================================
# 3. INSTAGRAM SENTIMENT BY CATEGORY
# ============================================================

instagram_cross = pd.crosstab(
    instagram["category"],
    instagram["sentiment_label_rater1"]
)

instagram_cross = instagram_cross.reindex(
    columns=["positive", "neutral", "negative"],
    fill_value=0
)

plt.figure(figsize=(10, 6))

instagram_cross.plot(
    kind="bar",
    ax=plt.gca()
)

plt.title("Instagram Sentiment by Content Category")
plt.xlabel("Content Category")
plt.ylabel("Number of Comments")
plt.xticks(rotation=0)

save_chart(
    "instagram_sentiment_by_category.png"
)

print("Created: instagram_sentiment_by_category.png")


# ============================================================
# 4. TWITTER BINARY SENTIMENT
# ============================================================

twitter_binary = (
    twitter_sentiment["sentiment"]
    .value_counts()
    .sort_index()
)

bar_chart(
    twitter_binary,
    "Twitter Binary Sentiment Distribution",
    "Sentiment Code",
    "Number of Posts",
    "twitter_binary_sentiment_distribution.png"
)

print("Created: twitter_binary_sentiment_distribution.png")


# ============================================================
# 5. TWITTER THREE-CLASS SENTIMENT
# ============================================================

twitter_three_class = (
    twitter_category["sentiment_label"]
    .value_counts()
    .reindex(
        ["positive", "neutral", "negative"],
        fill_value=0
    )
)

bar_chart(
    twitter_three_class,
    "Twitter Sentiment Distribution",
    "Sentiment",
    "Number of Posts",
    "twitter_sentiment_distribution.png"
)

print("Created: twitter_sentiment_distribution.png")


# ============================================================
# 6. YOUTUBE NOSTALGIA DISTRIBUTION
# ============================================================

youtube_nostalgia = (
    youtube_comments["sentiment"]
    .value_counts()
)

bar_chart(
    youtube_nostalgia,
    "YouTube Nostalgia Classification",
    "Classification",
    "Number of Comments",
    "youtube_nostalgia_distribution.png"
)

print("Created: youtube_nostalgia_distribution.png")


# ============================================================
# 7. YOUTUBE VIDEO CATEGORY DISTRIBUTION
# ============================================================

youtube_category = (
    youtube_videos["category"]
    .value_counts()
    .sort_values(ascending=False)
)

bar_chart(
    youtube_category,
    "YouTube Video Category Distribution",
    "Category",
    "Number of Videos",
    "youtube_video_category_distribution.png",
    rotation=45
)

print("Created: youtube_video_category_distribution.png")


# ============================================================
# 8. YOUTUBE VIEW COUNT DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    youtube_videos["view_count"].dropna(),
    bins=40
)

plt.title("Distribution of YouTube Video Views")
plt.xlabel("View Count")
plt.ylabel("Number of Videos")

save_chart(
    "youtube_view_count_distribution.png"
)

print("Created: youtube_view_count_distribution.png")


# ============================================================
# 9. YOUTUBE LIKE COUNT DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    youtube_videos["like_count"].dropna(),
    bins=40
)

plt.title("Distribution of YouTube Video Likes")
plt.xlabel("Like Count")
plt.ylabel("Number of Videos")

save_chart(
    "youtube_like_count_distribution.png"
)

print("Created: youtube_like_count_distribution.png")


# ============================================================
# 10. YOUTUBE VIEWS VS LIKES
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    youtube_videos["view_count"],
    youtube_videos["like_count"],
    alpha=0.6
)

plt.title("YouTube Views vs Likes")
plt.xlabel("View Count")
plt.ylabel("Like Count")

save_chart(
    "youtube_views_vs_likes.png"
)

print("Created: youtube_views_vs_likes.png")


# ============================================================
# 11. YOUTUBE AVERAGE LIKE RATE BY CATEGORY
# ============================================================

youtube_videos["like_rate"] = (
    youtube_videos["like_count"]
    / youtube_videos["view_count"]
    * 100
)

like_rate_by_category = (
    youtube_videos
    .groupby("category")["like_rate"]
    .mean()
    .sort_values(ascending=False)
)

bar_chart(
    like_rate_by_category,
    "Average YouTube Like Rate by Category",
    "Category",
    "Average Like Rate (%)",
    "youtube_like_rate_by_category.png",
    rotation=45
)

print("Created: youtube_like_rate_by_category.png")


# ============================================================
# 12. YOUTUBE AVERAGE VIEWS BY CATEGORY
# ============================================================

average_views = (
    youtube_videos
    .groupby("category")["view_count"]
    .mean()
    .sort_values(ascending=False)
)

bar_chart(
    average_views,
    "Average YouTube Views by Category",
    "Category",
    "Average Views",
    "youtube_average_views_by_category.png",
    rotation=45
)

print("Created: youtube_average_views_by_category.png")


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n" + "=" * 75)
print("              VISUALIZATION COMPLETE")
print("=" * 75)

print("\nAll charts were saved to:")
print(OUTPUT)
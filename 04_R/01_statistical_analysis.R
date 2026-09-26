# ============================================================
# SOCIAL MEDIA ANALYSIS PROJECT
# R STATISTICAL ANALYSIS
# ============================================================

# Set project directory
setwd("D:/Semester_III/DAT_Project")

# ------------------------------------------------------------
# 1. LOAD CLEANED DATASETS
# ------------------------------------------------------------

instagram <- read.csv(
  "02_Cleaned_Data/instagram_cleaned.csv",
  stringsAsFactors = FALSE
)

twitter_binary <- read.csv(
  "02_Cleaned_Data/twitter_sentiment_cleaned.csv",
  stringsAsFactors = FALSE
)

twitter_category <- read.csv(
  "02_Cleaned_Data/twitter_category_cleaned.csv",
  stringsAsFactors = FALSE
)

youtube_comments <- read.csv(
  "02_Cleaned_Data/youtube_comments_cleaned.csv",
  stringsAsFactors = FALSE
)

youtube_videos <- read.csv(
  "02_Cleaned_Data/youtube_videos_cleaned.csv",
  stringsAsFactors = FALSE
)

# ------------------------------------------------------------
# 2. CHECK DATASET DIMENSIONS
# ------------------------------------------------------------

cat("Instagram:", nrow(instagram), "rows,", ncol(instagram), "columns\n")
cat("Twitter Binary:", nrow(twitter_binary), "rows,", ncol(twitter_binary), "columns\n")
cat("Twitter Category:", nrow(twitter_category), "rows,", ncol(twitter_category), "columns\n")
cat("YouTube Comments:", nrow(youtube_comments), "rows,", ncol(youtube_comments), "columns\n")
cat("YouTube Videos:", nrow(youtube_videos), "rows,", ncol(youtube_videos), "columns\n")

# ------------------------------------------------------------
# 3. DISPLAY COLUMN NAMES
# ------------------------------------------------------------

cat("\nInstagram columns:\n")
print(names(instagram))

cat("\nTwitter Binary columns:\n")
print(names(twitter_binary))

cat("\nTwitter Category columns:\n")
print(names(twitter_category))

cat("\nYouTube Comments columns:\n")
print(names(youtube_comments))

cat("\nYouTube Videos columns:\n")
print(names(youtube_videos))
# ============================================================
# 4. DESCRIPTIVE STATISTICS
# ============================================================

cat("\n================ DESCRIPTIVE STATISTICS ================\n")

# ------------------------------------------------------------
# Instagram Likes
# ------------------------------------------------------------

cat("\nInstagram Likes:\n")
print(summary(instagram$likes))

# ------------------------------------------------------------
# Twitter Binary Sentiment
# ------------------------------------------------------------

cat("\nTwitter Binary Sentiment:\n")
print(table(twitter_binary$sentiment))

# ------------------------------------------------------------
# Twitter Three-Class Sentiment
# ------------------------------------------------------------

cat("\nTwitter Three-Class Sentiment:\n")
print(table(twitter_category$sentiment_label))

# ------------------------------------------------------------
# YouTube Nostalgia
# ------------------------------------------------------------

cat("\nYouTube Nostalgia:\n")
print(table(youtube_comments$sentiment))

# ------------------------------------------------------------
# YouTube Video Views
# ------------------------------------------------------------

cat("\nYouTube Views:\n")
print(summary(youtube_videos$view_count))

# ------------------------------------------------------------
# YouTube Likes
# ------------------------------------------------------------

cat("\nYouTube Likes:\n")
print(summary(youtube_videos$like_count))

# ------------------------------------------------------------
# YouTube Duration
# ------------------------------------------------------------

cat("\nYouTube Duration (seconds):\n")
print(summary(youtube_videos$duration_s))
# ============================================================
# 5. INSTAGRAM: CATEGORY vs SENTIMENT
#    CHI-SQUARE TEST OF INDEPENDENCE
# ============================================================

cat("\n================ INSTAGRAM CHI-SQUARE TEST ================\n")

# Create contingency table
instagram_table <- table(
  instagram$category,
  instagram$sentiment_label_rater1
)

cat("\nContingency Table:\n")
print(instagram_table)

# Chi-square test
instagram_chisq <- chisq.test(instagram_table)

cat("\nChi-square Test Result:\n")
print(instagram_chisq)

cat("\nExpected Frequencies:\n")
print(instagram_chisq$expected)
# ============================================================
# 6. SAVE INSTAGRAM CHI-SQUARE RESULT
# ============================================================

instagram_chisq_result <- data.frame(
  test = "Chi-square test of independence",
  variable_1 = "Instagram category",
  variable_2 = "Instagram sentiment",
  chi_square = as.numeric(instagram_chisq$statistic),
  degrees_of_freedom = as.numeric(instagram_chisq$parameter),
  p_value = instagram_chisq$p.value
)

write.csv(
  instagram_chisq_result,
  "09_Analysis_Output/instagram_chisquare_result.csv",
  row.names = FALSE
)
# ============================================================
# 7. YOUTUBE: VIEWS vs LIKES
#    PEARSON CORRELATION TEST
# ============================================================

cat("\n================ YOUTUBE CORRELATION TEST ================\n")

youtube_correlation <- cor.test(
  youtube_videos$view_count,
  youtube_videos$like_count,
  method = "pearson",
  use = "complete.obs"
)

cat("\nPearson Correlation Test Result:\n")
print(youtube_correlation)
twitter_sentiment_data$sentiment_name <- ifelse(
  twitter_sentiment_data$sentiment == 1,
  "Positive",
  "Negative"
)

twitter_sentiment_summary <- as.data.frame(
  table(twitter_sentiment_data$sentiment_name)
)

colnames(twitter_sentiment_summary) <- c(
  "Sentiment",
  "Count"
)

twitter_sentiment_percentage <- prop.table(
  table(twitter_sentiment_data$sentiment_name)
) * 100


twitter_category_data$category_name <- ifelse(
  twitter_category_data$category == 1,
  "Positive",
  ifelse(
    twitter_category_data$category == 0,
    "Neutral",
    "Negative"
  )
)

twitter_category_summary <- as.data.frame(
  table(twitter_category_data$category_name)
)


instagram_category_summary <- as.data.frame(
  table(instagram_data$category)
)

colnames(instagram_category_summary) <- c(
  "Category",
  "Count"
)


instagram_sentiment_summary <- as.data.frame(
  table(instagram_data$sentiment_label_rater1)
)

colnames(instagram_sentiment_summary) <- c(
  "Sentiment",
  "Count"
)


instagram_likes_summary <- summary(
  instagram_data$likes
)


youtube_category_summary <- as.data.frame(
  table(youtube_data2$category)
)

colnames(youtube_category_summary) <- c(
  "Category",
  "Count"
)


youtube_views_summary <- summary(
  youtube_data2$view_count,
  na.rm = TRUE
)

youtube_likes_summary <- summary(
  youtube_data2$like_count,
  na.rm = TRUE
)


youtube_data2$engagement_rate <- (
  youtube_data2$like_count /
  youtube_data2$view_count
) * 100


top_views <- youtube_data2[
  order(
    youtube_data2$view_count,
    decreasing = TRUE,
    na.last = NA
  ),
]

top_10_views <- head(top_views, 10)


top_likes <- youtube_data2[
  order(
    youtube_data2$like_count,
    decreasing = TRUE,
    na.last = NA
  ),
]

top_10_likes <- head(top_likes, 10)


average_views <- aggregate(
  view_count ~ category,
  data = youtube_data2,
  FUN = mean,
  na.rm = TRUE
)


average_likes <- aggregate(
  like_count ~ category,
  data = youtube_data2,
  FUN = mean,
  na.rm = TRUE
)
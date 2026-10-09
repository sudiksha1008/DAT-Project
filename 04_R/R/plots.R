twitter_sentiment_bar <- function() {
  barplot(
    twitter_sentiment_summary$Count,
    names.arg = twitter_sentiment_summary$Sentiment,
    main = "Twitter Sentiment Distribution",
    xlab = "Sentiment",
    ylab = "Number of Tweets"
  )
}

twitter_sentiment_pie <- function() {
  pie(
    twitter_sentiment_percentage,
    labels = paste(
      names(twitter_sentiment_percentage),
      round(twitter_sentiment_percentage, 2),
      "%"
    ),
    main = "Twitter Sentiment Percentage"
  )
}

twitter_category_bar <- function() {
  barplot(
    twitter_category_summary$Count,
    names.arg = twitter_category_summary$Category,
    main = "Twitter Category Distribution",
    xlab = "Category",
    ylab = "Number of Tweets"
  )
}

twitter_category_pie <- function() {
  pie(
    twitter_category_percentage,
    labels = paste(
      names(twitter_category_percentage),
      round(twitter_category_percentage, 2),
      "%"
    ),
    main = "Twitter Category Percentage"
  )
}

instagram_category_bar <- function() {
  barplot(
    instagram_category_summary$Count,
    names.arg = instagram_category_summary$Category,
    main = "Instagram Category Distribution",
    xlab = "Category",
    ylab = "Number of Posts"
  )
}

instagram_sentiment_bar <- function() {
  barplot(
    instagram_sentiment_summary$Count,
    names.arg = instagram_sentiment_summary$Sentiment,
    main = "Instagram Sentiment Distribution",
    xlab = "Sentiment",
    ylab = "Number of Posts"
  )
}

instagram_likes_histogram <- function() {
  hist(
    instagram_data$likes,
    main = "Instagram Likes Distribution",
    xlab = "Likes",
    ylab = "Number of Posts"
  )
}

youtube_sentiment_bar <- function() {
  barplot(
    youtube_sentiment_summary$Count,
    names.arg = youtube_sentiment_summary$Sentiment,
    main = "YouTube Sentiment Distribution",
    xlab = "Sentiment",
    ylab = "Number of Comments"
  )
}

youtube_sentiment_pie <- function() {
  pie(
    youtube_sentiment_percentage,
    labels = paste(
      names(youtube_sentiment_percentage),
      round(youtube_sentiment_percentage, 2),
      "%"
    ),
    main = "YouTube Sentiment Percentage"
  )
}

youtube_category_bar <- function() {
  barplot(
    youtube_category_summary$Count,
    names.arg = youtube_category_summary$Category,
    main = "YouTube Category Distribution",
    xlab = "Category",
    ylab = "Number of Videos",
    las = 2
  )
}

youtube_views_histogram <- function() {
  hist(
    youtube_data2$view_count,
    main = "YouTube Views Distribution",
    xlab = "Views",
    ylab = "Number of Videos"
  )
}

youtube_likes_histogram <- function() {
  hist(
    youtube_data2$like_count,
    main = "YouTube Likes Distribution",
    xlab = "Likes",
    ylab = "Number of Videos"
  )
}

youtube_engagement_histogram <- function() {
  hist(
    youtube_data2$engagement_rate,
    main = "YouTube Engagement Rate Distribution",
    xlab = "Engagement Rate (%)",
    ylab = "Number of Videos"
  )
}

youtube_top_views_bar <- function() {
  barplot(
    top_10_views$view_count,
    names.arg = 1:10,
    main = "Top 10 Most Viewed YouTube Videos",
    xlab = "Video Rank",
    ylab = "Number of Views"
  )
}

youtube_top_likes_bar <- function() {
  barplot(
    top_10_likes$like_count,
    names.arg = 1:10,
    main = "Top 10 Most Liked YouTube Videos",
    xlab = "Video Rank",
    ylab = "Number of Likes"
  )
}

youtube_average_views_bar <- function() {
  barplot(
    average_views$view_count,
    names.arg = average_views$category,
    main = "Average Views by YouTube Category",
    xlab = "Category",
    ylab = "Average Views",
    las = 2
  )
}

youtube_average_likes_bar <- function() {
  barplot(
    average_likes$like_count,
    names.arg = average_likes$category,
    main = "Average Likes by YouTube Category",
    xlab = "Category",
    ylab = "Average Likes",
    las = 2
  )
}
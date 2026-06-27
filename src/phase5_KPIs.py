import pandas as pd
from collections import Counter
from pymongo import MongoClient

# Load Data from MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["reviews"]

data = list(collection.find())
df = pd.DataFrame(data)
# Total Reviews
total_reviews = len(df)


# Overall Satisfaction KPI
positive_rate = (df["sentiment"] == "positive").mean()
print("Satisfaction Rate:" , positive_rate )

# Average Rating
avg_rating = df["rating"].mean()
print("Average Rating:" , avg_rating)

# Sentiment Distribution
sentiment_counts = df["sentiment"].value_counts()
print(sentiment_counts)

# Top Products & Worst Products
top_products = (df.groupby("title")["rating"]
                .mean()
                .sort_values(ascending=False)
                .head(10)
                )
worst_products = (df.groupby("title")["rating"]
                  .mean()
                  .sort_values()
                  .head(10)
                  )
print(top_products , "\n" , worst_products)

# Reviews Over Time
df["reviewTime"] = pd.to_datetime(df["reviewTime"])
reviews_over_time = df.groupby(df["reviewTime"].dt.year).size()
print(reviews_over_time)

# Export for Power BI
df.to_csv("data/processed/reviews_with_sentiment.csv" , index = False)

sentiment_counts.to_csv("data/processed/Power BI/sentiment_distribution.csv")
top_products.to_csv("data/processed/Power BI Data/top_products.csv")
worst_products.to_csv("data/processed/Power BI/worst_products.csv")
reviews_over_time.to_csv("data/processed/Power BI//reviews_over_time.csv")

# Turn positive_rate and avg_rating into a kpi dataframe to export it as .csv so we can use it later in Power BI
kpi_df = pd.DataFrame({
    ["Total Reviews" , "Positive Rate" , "Average Rating"],
    [total_reviews , positive_rate , avg_rating]
})
kpi_df.to_csv("data/processed/Power BI/kpis.csv" , index= False)


df = pd.read_csv("data/processed/reviews_with_sentiment.csv")
df = df.dropna(subset=["clean_text"])

df["clean_text"] = df["clean_text"].astype(str)

# split words
all_words = " ".join(df["clean_text"]).split()

# count words
word_counts = Counter(all_words)

# get top 20
top_words = pd.DataFrame(word_counts.most_common(20), columns=["word" , "count"])

print(top_words)

# export for Power BI
top_words.to_csv("data/processed/Power BI/top_words.csv" , index = False)
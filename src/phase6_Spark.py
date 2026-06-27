from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, when, to_date
import pandas as pd

# Create Spark Session
spark = SparkSession.builder \
    .appName("Amazon Reviews Big Data KPIs") \
    .getOrCreate()
print("Spark Session started")


# Load Dataset
file_path = "amazon_reveiews_project/data/processed/reviews_with_sentiment.csv"
df = spark.read.csv(file_path, header= True, inferSchema=True)
print("Dataset loaded")
df.show(5)

# Convert Date Column
df = df.withColumn("reviewTime" ,to_date(col("reviewTime")))

# Overall Satisfaction Rate
total_reviews = df.count()
positive_reviews = df.filter(col("predicted_sentiment") == "positive").count()
satisfaction_rate = positive_reviews/total_reviews
print("Satisfaction Rate:", satisfaction_rate)

# Average Rating
average_rating = df.select(avg("rating")).collect()[0][0]
print("Average Rating:" , average_rating)

# Save those 2 KPIs
kpi_df = pd.DataFrame({
    "metric" : ["average_rating", "satisfaction_rate" , "total_reviews"],
    "value" : [average_rating , satisfaction_rate , total_reviews]
})
kpi_df.to_csv("amazon_reveiews_project/data/processed/spark_output/kpi_summary.csv" , index = False)
print("Average Rating & Satisfaction Rate Saved")

# Sentiment Distribution
sentiment_dist = df.groupBy("predicted_sentiment") \
    .agg(count("*").alias("count"))
sentiment_dist_pd = sentiment_dist.toPandas()
sentiment_dist_pd.to_csv("amazon_reveiews_project/data/processed/spark_output/sentiment_distribution.csv")
print("Sentiment Distribution Saved")

# Top Products
top_products = df.groupBy("title") \
    .agg(avg("rating").alias("avg_rating"),
count("*").alias("num_reviews")) \
    .orderBy(col("avg_rating").desc())
top_products_pd = top_products.toPandas()
top_products_pd.to_csv("amazon_reveiews_project/data/processed/spark_output/top_products.csv" , index = False)
print("Top Products Saved")

# Worst Products
worst_products = df.groupBy("title") \
    .agg(avg("rating").alias("avg_rating"),
count("*").alias("num_reviews")) \
    .orderBy(col("avg_rating").asc())
worst_products_pd = worst_products.toPandas()
worst_products_pd.to_csv("amazon_reveiews_project/data/processed/spark_output/worst_products.csv" , index = False)
print("Worst Products Saved")

# Reviews Over Time
reviews_over_time = df.groupBy("reveiewTime") \
    .agg(count("*").alias("num_reviews")) \
    .orderBy("reviewTime")
reviews_over_time_pd = reviews_over_time.toPandas()
reviews_over_time_pd.to_csv("amazon_reveiews_project/data/processed/spark_output/reviews_over_time.csv" , index = False)
print("Reviews Over Time Saved")

# Stop Spark Session
spark.stop()
print("Spark Session Stopped")
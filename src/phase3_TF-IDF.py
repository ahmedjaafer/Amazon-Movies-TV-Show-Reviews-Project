from pymongo import MongoClient
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["reviews"]

# Load data
data = list(collection.find())
df = pd.DataFrame(data)

print("Data loaded:", df.shape)

# Drop MongoDB ID
if "_id" in df.columns:
    df = df.drop(columns=["_id"])

# Keep only needed columns
df = df[["clean_text", "sentiment"]]

# Remove empty values
df = df.dropna()

print("Dataset after cleaning:", df.shape)

# Sample dataset for faster TF-IDF
print("Sampling 200,000 reviews...")
df = df.sample(200000, random_state=42)

print("Sampled dataset shape:", df.shape)

# Text column
X_text = df["clean_text"]

# Target column
y = df["sentiment"]

print("Creating TF-IDF vectors...")

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english",
    min_df=5
)

X = vectorizer.fit_transform(X_text)
print("TF-IDF completed")
print("Feature matrix shape:", X.shape)

# Save Processed Data
pickle.dump((X, y, vectorizer), open("data/processed_data.pkl", "wb"))
print("Phase 3 data saved successfully")
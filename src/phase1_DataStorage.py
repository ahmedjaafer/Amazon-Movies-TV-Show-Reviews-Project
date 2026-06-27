import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Reading the dataset
df = pd.read_json("data/raw/dataset_Movies_And_TV.json", lines = True)
print("Reading dataset completed")

# Keep Only Useful Columns
df= df[['reviewText', 'overall', 'reviewTime', 'asin','title']]
df.rename(columns={'overall' : 'rating'}, inplace=True)

'''
# Reading the metadata file , it didnt wanna be read using pandas read_json() because its not true json so we gonna use this method
import ast
path = r"data/raw/meta_Movies_And_TV.json"
data = []
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        data.append(ast.literal_eval(line))
meta = pd.DataFrame(data)
meta = meta [['asin','title']]
print("Reading metadata completed")
print(meta.shape)
print(meta.columns)
print(meta.isna().sum())

# JOIN metadata and the review dataset
df = df.merge(meta ,on='asin' , how='left')
print("Merging completed")
'''
# Replace Null titles with "Unknown Product"
df["title"] = df["title"].fillna("Unknown Product")

# Create Sentiment Label
def label_sentiment (rating):
    if rating >=4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"
df['sentiment'] = df['rating'].apply(label_sentiment)
print(df["sentiment"].value_counts())

# Save Clean Data
df.to_csv("data/processed/amazon_reviews_clean.csv" , index = False)
print("Saving CSV file completed")
# Store Data in MongoDB
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["reviews"]
collection.insert_many(df.to_dict("records"))
print(df.columns)

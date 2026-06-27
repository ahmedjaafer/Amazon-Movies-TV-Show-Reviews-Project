# Download NLTK Resources
import nltk
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')
#nltk.download('wordnet')
# Only run them once


from pymongo import MongoClient
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Importing NLP Libraries
import re # text cleaning (regex)
from nltk.tokenize import word_tokenize # split text into words
from nltk.corpus import stopwords # remove useless words
from nltk.stem import WordNetLemmatizer # convert words to base form

# LOAD DATA FROM MONGODB

client = MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["reviews"]

data = list(collection.find()) # gets all documents and converts them to python list
df = pd.DataFrame(data) # converts list to a dataframe

print("Data loaded:", df.shape) # shows the number of rows and columns

# NLP TOOLS

stop_words = set(stopwords.words("english")) # set the language of the stopwords we wanna remove to english, makes the search faster (words like the ,is ,and ,a ,to , of)
# Remove important words from stopwords list
important_words = {"not", "no", "nor", "but"}
stop_words = stop_words - important_words

lemmatizer = WordNetLemmatizer() # convert for example running → run , cars → car , better → good

# CLEANING FUNCTION (this function cleans 1 review at a time)

def preprocess_text(text):
    
    if pd.isna(text): # if review is empty ,return empty string (avoid errors)
        return ""
    
    # Lowercase
    text = text.lower()
    
    # Remove punctuation & numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Tokenization
    tokens = word_tokenize(text) # split sentence into words (example : "this product is amazing" → ["this", "product", "is", "amazing"])
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words] # ["this", "product", "is", "amazing"] → ["product", "amazing"]

    
    # Lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens] # ["products", "running"] → ["product", "run"]
    
    return " ".join(tokens) # join tokens back to a sentence (["product", "amazing"] → "product amazing")

# Apply preprocessing & New column called "clean_text"
df["clean_text"] = df["reviewText"].apply(preprocess_text)
for i, row in df.iterrows():
    collection.update_one(
        {"_id": row["_id"]},
        {"$set": {"clean_text": row["clean_text"]}}
    )

print("Text preprocessing done")
print(df.head(10))
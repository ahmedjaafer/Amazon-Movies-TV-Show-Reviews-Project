# Big Data Analytics & Sentiment Analysis of Amazon Movies & TV Reviews

## Final Year Project (Bachelor's Degree in Big Data & Data Analytics)

This repository contains my **Final Year Project (Bachelor's Degree in Big Data & Data Analytics)**, which was successfully defended and awarded **Highest Honors**.

The project focuses on building an end-to-end Big Data analytics pipeline capable of processing large-scale Amazon customer reviews, performing sentiment analysis using Natural Language Processing (NLP) and Machine Learning, generating business KPIs, and visualizing insights through interactive Power BI dashboards.

---

# Project Objectives

The main objectives of this project are:

- Store and manage large-scale review data using MongoDB.
- Clean and preprocess textual data.
- Apply NLP techniques for text processing.
- Transform text into numerical features using TF-IDF.
- Train and evaluate Machine Learning models for sentiment classification.
- Generate business KPIs.
- Build interactive Power BI dashboards for business intelligence.
- Demonstrate scalable data processing using PySpark.

---

# Dataset

**Dataset:** Amazon Movies & TV Reviews

The dataset contains approximately **1.7 million customer reviews** collected from the beginning of Amazon's review history up to **2014**.

The project uses:

- Customer reviews
- Product metadata
- Ratings
- Product identifiers
- Review timestamps

The review dataset was merged with product metadata to enrich the analysis.

Both the dataset and its metadata were downloaded from the UCSD website : https://cseweb.ucsd.edu/~jmcauley/datasets/amazon/links.html

---

# Technologies Used

### Programming

- Python

### Database

- MongoDB (Pymongo)

### Data Processing

- Pandas

### Natural Language Processing

- NLTK

### Machine Learning

- Scikit-learn
- Logistic Regression
- Linear Support Vector Classifier (Linear SVC)

### Feature Engineering

- TF-IDF Vectorization

### Big Data

- PySpark

### Business Intelligence

- Power BI

### Serialization

- Pickle

---

# Project Workflow

```
Dataset
    │
    ▼
MongoDB Storage
    │
    ▼
Data Cleaning
    │
    ▼
NLP Preprocessing
    │
    ▼
TF-IDF Feature Engineering
    │
    ▼
Machine Learning
    │
    ├────────► Sentiment Prediction
    │
    ▼
KPI Generation
    │
    ▼
Power BI Dashboards
```

---

# Project Structure

```
amazon-reviews-project/
│
├── data/
│   ├── raw/
|       ├── dataset_Movies_And_TV.json
|       ├── meta_Movies_And_TV.json
│   ├── processed/
|       ├── amazon_reviews_clean.csv
|       ├── reviews_with_sentiment.csv
|       ├── Power BI
|          ├── kpis.csv
|          ├── dashboard_data.csv
|          ├── reviews_over_time.csv
|          ├── sentiment_distribution.csv
|          ├── top_products.csv
|          ├── worst products.csv
|          ├── top_words.csv
│   ├── spark_output/    
│   └── processed_data.pkl
│
├── models/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── dashboard/
│   └── Project Dashboard.pbix
│
├── src/
|   ├── phase1_import.py
│   ├── phase2_preprocessing.py
│   ├── phase3_tfidf.py
│   ├── phase4_machine_learning.py
│   ├── phase5_kpi_generation.py
│   ├── phase6_spark.py
│
└── report/
|   ├── report.pdf
```

---

# Data Preprocessing

The preprocessing pipeline includes:

- Missing value handling
- Duplicate removal
- Text normalization
- Lowercase conversion
- Removal of punctuation
- Removal of numbers
- Removal of special characters
- Extra whitespace removal
- Tokenization
- Stopword removal
- Negation handling
- Sentiment label creation

---

# Feature Engineering

The project uses **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert customer reviews into numerical vectors suitable for machine learning.

A representative sample of **200,000 reviews** was vectorized.

The resulting sparse matrix was saved using **Pickle** to avoid recomputing the vectorization process during model experimentation.

---

# Machine Learning

Two supervised learning algorithms were evaluated:

- Logistic Regression
- Linear Support Vector Classifier (Linear SVC)

### Results

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **81.89%** |
| Linear SVC | **81.82%** |

Although both models achieved very similar performance, Logistic Regression was selected as the final model based on its slightly higher accuracy.

---

# Big Data Processing

Although the primary machine learning pipeline was implemented using Python libraries, **PySpark** was integrated to demonstrate scalable Big Data processing.

PySpark was used to reproduce KPI generation and aggregation operations in a distributed environment, illustrating how the solution can be extended to much larger datasets.

---

# Business KPIs

The project generates several business indicators, including:

- Total Reviews
- Average Rating
- Sentiment Distribution
- Positive Review Percentage
- Review Trends
- Product Rankings
- Product Performance Metrics

These KPIs serve as the foundation for the Power BI dashboards.

---

# Power BI Dashboard

Interactive dashboards were created to support business analysis.

Dashboard pages include:

- Overview
- Customer Review Insights
- Product Performance Analysis
- Review Trends

The dashboards enable users to explore customer satisfaction, sentiment evolution, product popularity, and review behavior through interactive visualizations.

---

# Key Features

✔ Large-scale customer review processing

✔ NLP-based text preprocessing

✔ TF-IDF feature engineering

✔ Machine Learning sentiment classification

✔ Business KPI generation

✔ Interactive Power BI dashboards

✔ Scalable PySpark processing

---

# Future Improvements

Possible extensions include:

- Transformer-based models (BERT, RoBERTa)
- Aspect-Based Sentiment Analysis
- Real-time review processing
- Web application deployment
- Cloud-based distributed processing

---

# Academic Achievement

This project was completed as my **Bachelor's Final Year Project in Big Data & Data Analytics** at ISIMS Sfax, Tunisia and was successfully defended with **Highest Honors**.

---

# Author

**Ahmed Jaafar**

Bachelor's Degree in Big Data & Data Analytics

Feel free to connect with me on LinkedIn or explore my other projects on GitHub.
LinkedIn: https://www.linkedin.com/in/ahmed-jaafar-876b0a3a0
Github: https://github.com/ahmedjaafer

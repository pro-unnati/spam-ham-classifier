import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spam.csv")

df.head()
df.isnull().sum()
df.shape
df.columns
df.dtypes
print("Duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
df.head()
df.shape()


X = df["Message"]
y = df["Category"]

X.head()
print(y.value_counts())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))



from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# Features and target
X = df["Message"].astype(str)   # SMS text column
y = df["Category"].str.lower().str.strip()  # Spam/Ham label column

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create the text classification pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])



import joblib

joblib.dump(model, "spam_ham_model.pkl")

print("Model saved successfully!")
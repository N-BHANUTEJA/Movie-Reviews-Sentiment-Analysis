# -*- coding: utf-8 -*-
"""Sentiment Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11SzZfH-j9IDjWJxsRMqskGgU2xCD07ON

# **Sentiment Analysis On Movie Reviews**

**1. Dataset Collection**

Zipfile Extraction
"""

import zipfile
import os

# Define the path to the zip file
zip_file_path = '/content/Movie Reviews.zip'  # Replace with your actual path

# Extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall("/content/")  # Extract files to the content folder

# List the extracted files to confirm
extracted_files = os.listdir("/content/")
print(extracted_files)

"""**2. Data Preprocessing**

We'll load the data, inspect it, and clean it up if necessary. Typically, the steps involved in preprocessing are:

**Loading the data:** We'll load the dataset into a pandas DataFrame.

**Inspecting the data:** Check for missing values, irrelevant columns, and basic statistics.

**Text cleaning:** Remove unwanted characters, stopwords, and normalize the text.

**Label encoding:** Convert the target variable (positive/negative) into numerical format.
"""

import pandas as pd

# Load the dataset
file_path = '/content/IMDB Dataset.csv'  # Update with your actual file path
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
df.head()

"""**3. Text Cleaning**

In sentiment analysis, it's essential to clean the text data to remove noise and irrelevant information. The typical steps are:

Convert text to lowercase

Remove punctuation, special characters, and numbers

Tokenize text (split into words)

Remove stopwords (commonly used words like 'the', 'is', 'in', etc.)

Lemmatization (reduce words to their base form, e.g., 'running' to 'run')
"""

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
# Download the punkt_tab data package
nltk.download('punkt_tab') # This line is added to download the required data

# Initialize lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove non-alphabetic characters (punctuation, numbers, etc.)
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize the text
    words = nltk.word_tokenize(text)

    # Remove stopwords and lemmatize
    cleaned_text = ' '.join([lemmatizer.lemmatize(word) for word in words if word not in stop_words])

    return cleaned_text

# Apply the cleaning function to the review text column (replace 'review' with your actual column name)
df['cleaned_reviews'] = df['review'].apply(clean_text)

# Display the first few rows of the cleaned data
df[['review', 'cleaned_reviews']].head()

"""**4. Text Vectorization**

To prepare the text for a machine learning model, we need to convert the cleaned text into numerical format.

This is done using text vectorization techniques like:

**Bag of Words (BoW):** Represents text data as a matrix of word counts.

**TF-IDF:** Weighs words based on their frequency and importance.
"""

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)  # Use the top 5000 features

# Fit and transform the cleaned reviews into a numerical format
X = vectorizer.fit_transform(df['cleaned_reviews']).toarray()

# Display the shape of the resulting matrix
print(X.shape)

"""**5. Model Training**

We'll train a machine learning model to predict the sentiment of the movie reviews (positive or negative). For sentiment analysis, Logistic Regression is a good starting point, but we can also try other models like Naive Bayes or Support Vector Machines (SVM).

We’ll follow these steps:

**Split** the dataset into training and testing sets.

**Train** the model using the training data.

**Evaluate** the model using the test data.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Assuming 'sentiment' is the column that contains the labels (0 for negative, 1 for positive)
# Replace 'sentiment' with the actual column name in your dataset
y = df['sentiment']  # Labels
X = vectorizer.fit_transform(df['cleaned_reviews']).toarray()  # Features

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Display the results
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

"""**6. Testing the Model on New Data**

To test the model on new, unseen data (i.e., a new movie review), we'll follow these steps:

Clean the new review text (using the same cleaning function we used before).

Vectorize the cleaned text using the same TF-IDF vectorizer.

Make predictions using the trained model.

Here’s the code to test the model on new reviews:
"""

# Function to predict sentiment for a new review
def predict_sentiment(new_review):
    # Clean the new review
    cleaned_review = clean_text(new_review)

    # Vectorize the cleaned review
    vectorized_review = vectorizer.transform([cleaned_review]).toarray()

    # Make prediction
    prediction = model.predict(vectorized_review)

    # Return the sentiment (0 for negative, 1 for positive)
    return "Positive" if prediction == 1 else "Negative"

# Test the model on a new review
new_review = "The movie was a complete disaster. The plot was predictable and the acting was subpar."
print(f"Predicted sentiment: {predict_sentiment(new_review)}")

# Make predictions on the test set
predictions = model.predict(X_test)

# Print the original and predicted values (for debugging purposes)
print("Original:", y_test.values)
print("Predicted:", predictions)

# Calculate the number of correct predictions
correct_prediction = 0
for i in range(len(predictions)):
    if predictions[i] == y_test.iloc[i]:  # Comparing the predictions to the true labels
        correct_prediction += 1

# Calculate and print the percentage of correct predictions
correct_percentage = (correct_prediction * 100) / len(predictions)
print(f"Correctly predicted percentage: {correct_percentage:.2f}%")

"""# **Importing and Training the Naive Bayes Model**"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Vectorize the reviews using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features based on the dataset size
X = vectorizer.fit_transform(df['cleaned_reviews']).toarray()  # Use 'cleaned_reviews' column

# The target variable is the sentiment (positive or negative)
Y = df['sentiment']  # Assuming sentiment column is already encoded as 0 and 1

# Split the data into training and test sets (80% training, 20% test)
X_train_tfidf, X_test_tfidf, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes model
nb_model = MultinomialNB()

# Train the model
nb_model.fit(X_train_tfidf, Y_train)

# Make predictions
nb_predictions = nb_model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(Y_test, nb_predictions)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(Y_test, nb_predictions))

# Classification Report
print("Classification Report:")
print(classification_report(Y_test, nb_predictions))

# Import the necessary libraries (if not already done)
from sklearn.feature_extraction.text import TfidfVectorizer

# Assuming you have the 'df' DataFrame and 'clean_text' function already defined as before
# Define and fit the TfidfVectorizer on the training data
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features as needed
X_train_tfidf = tfidf_vectorizer.fit_transform(df['cleaned_reviews'])  # Use the cleaned reviews from your DataFrame

# Example new reviews
new_reviews = [
    "This movie was absolutely amazing, I loved every second of it! The acting was great and the plot was engaging.",
    "The movie was terrible. The plot was boring, and the acting was subpar. I wouldn't recommend it."
]

# Preprocess the new reviews using the same cleaning function
new_reviews_cleaned = [clean_text(review) for review in new_reviews]

# Convert the cleaned reviews into the same feature format as the training data (TF-IDF)
new_reviews_tfidf = tfidf_vectorizer.transform(new_reviews_cleaned)

# Use the trained Naive Bayes model to predict the sentiment of the new reviews
predictions = nb_model.predict(new_reviews_tfidf)

# Display the predictions
for i, review in enumerate(new_reviews):
    print(f"Review {i+1}: {review}")
    print(f"Predicted Sentiment: {'Positive' if predictions[i] == 1 else 'Negative'}\n")

import pandas as pd

# Load the dataset (make sure the correct path to the file is provided)
df = pd.read_csv('/content/IMDB Dataset.csv')

# If your dataset is already in the environment, just load it into df
# For example, if it’s in a file named 'reviews.csv' in the same folder:
df = pd.read_csv('IMDB Dataset.csv')

# Check the first few rows of the dataset and its columns
df.head()
df.columns

# Check the columns of the dataframe
print(df.columns)

# Assuming the clean_text function is already defined
df['cleaned_reviews'] = df['review'].apply(clean_text)

# Check the first few rows to make sure it's working
print(df[['review', 'cleaned_reviews']].head())

from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the vectorizer with max features and n-grams (unigrams and bigrams)
tfidf_vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))

# Fit and transform the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(df['cleaned_reviews'])

# If you have a separate test dataset, transform it with the same vectorizer
# Assuming you have a column 'cleaned_reviews_test' for testing data, if not you can split the data manually
X_test_tfidf = tfidf_vectorizer.transform(df['cleaned_reviews'])  # For the same dataset

from sklearn.model_selection import train_test_split

# Split your data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(df['cleaned_reviews'], df['sentiment'], test_size=0.2, random_state=42)

# Now, transform both train and test data
tfidf_vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 3))
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Train the Naive Bayes model
nb_model.fit(X_train_tfidf, Y_train)

# Predict on the test data
Y_pred = nb_model.predict(X_test_tfidf)

# Check accuracy
accuracy = (Y_pred == Y_test).mean()
print(f"Accuracy: {accuracy * 100:.2f}%")

# Check the shape of the transformed data
print(X_train_tfidf.shape)
print(X_test_tfidf.shape)

"""**Train the Naive Bayes model**"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Assuming you have the sentiment labels in 'sentiment' column
X = X_train_tfidf
Y = df['sentiment']

# Split the data into training and testing sets (if you haven't already)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes model
nb_model = MultinomialNB()

# Train the model on the training data
nb_model.fit(X_train, Y_train)

# Make predictions on the test data
predictions = nb_model.predict(X_test)

# Evaluate the model
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print(f"Accuracy: {accuracy_score(Y_test, predictions) * 100:.2f}%")
print("Confusion Matrix:")
print(confusion_matrix(Y_test, predictions))
print("Classification Report:")
print(classification_report(Y_test, predictions))

# Define new reviews
new_reviews = [
    "This movie was amazing! I loved every bit of it, definitely worth watching.",
    "Worst movie ever, a total waste of time."
]

# Clean the new reviews
new_reviews_cleaned = [clean_text(review) for review in new_reviews]

# Transform the cleaned reviews using the same TF-IDF vectorizer
new_reviews_tfidf = tfidf_vectorizer.transform(new_reviews_cleaned)

# Make predictions on the new reviews
new_predictions = nb_model.predict(new_reviews_tfidf)

# Output the predictions
for review, prediction in zip(new_reviews, new_predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(f"Review: {review}\nSentiment: {sentiment}\n")

"""**Hypertuning**"""

from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Prepare the TF-IDF vectorizer again if it's not already done
tfidf_vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Define the Naive Bayes model
nb_model = MultinomialNB()

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'alpha': [0.1, 0.5, 1.0, 2.0, 5.0]  # Alpha is the smoothing parameter for Naive Bayes
}

# Set up the GridSearchCV
grid_search = GridSearchCV(estimator=nb_model, param_grid=param_grid, cv=5, verbose=1, n_jobs=-1)

# Fit GridSearchCV to the training data
grid_search.fit(X_train_tfidf, Y_train)

# Get the best hyperparameters
print(f"Best Hyperparameters: {grid_search.best_params_}")

# Use the best model from GridSearchCV
best_model = grid_search.best_estimator_

# Predict on the test data
Y_pred = best_model.predict(X_test_tfidf)

# Check accuracy
accuracy = (Y_pred == Y_test).mean()
print(f"Accuracy after Hyperparameter Tuning: {accuracy * 100:.2f}%")

# If needed, you can check classification report and confusion matrix as well:
from sklearn.metrics import classification_report, confusion_matrix

print("Confusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))

print("Classification Report:")
print(classification_report(Y_test, Y_pred))

# Assuming you have already cleaned the reviews and have training data (X_train_tfidf and Y_train)

# Train the Naive Bayes model on the training data
nb_model.fit(X_train_tfidf, Y_train)

# New reviews (5 positive and 5 negative)
new_reviews = [
    "The movie was fantastic! The plot was gripping and the acting was superb. Highly recommend it!",  # Positive
    "I absolutely loved this film. The direction and screenplay were top-notch, a must-watch for movie lovers.",  # Positive
   "A waste of two hours. The movie was filled with clichés and had no real depth or emotion.",  # Negative
    "The worst movie I've seen in a long time. The acting was subpar and the plot was all over the place."  # Negative
]

# Clean the new reviews (using the same cleaning function from before)
new_reviews_cleaned = [clean_text(review) for review in new_reviews]

# Convert the cleaned reviews into the same feature format as the training data (TF-IDF)
new_reviews_tfidf = tfidf_vectorizer.transform(new_reviews_cleaned)

# Use the trained Naive Bayes model to predict the sentiment of the new reviews
new_predictions = nb_model.predict(new_reviews_tfidf)

# Display the results
for review, prediction in zip(new_reviews, new_predictions):
    sentiment = "Positive" if prediction == 1 else "Negative"
    print(f"Review: {review}\nSentiment: {sentiment}\n")

print(df['sentiment'].value_counts())  # To check the number of positive and negative labels in the dataset

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

# Check the shapes of the splits
print("Training data size:", X_train.shape)
print("Test data size:", X_test.shape)

from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF Vectorization with unigrams, bigrams, and trigrams, and top 8000 features
tfidf_vectorizer = TfidfVectorizer(max_features=8000, ngram_range=(1, 3))  # Unigrams, bigrams, trigrams

# Fit the vectorizer on the training data and transform it
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data using the same vectorizer
X_test_tfidf = tfidf_vectorizer.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Train the Naive Bayes model
nb_model = MultinomialNB(alpha=0.1)  # Use the optimal alpha from hyperparameter tuning
nb_model.fit(X_train_tfidf, Y_train)

# Predict on the test set
Y_pred = nb_model.predict(X_test_tfidf)

# Evaluate the model
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("Classification Report:\n", classification_report(Y_test, Y_pred))

# New reviews for testing
new_reviews = [
    "This movie was fantastic, I loved it!",
    "Horrible movie, I regret watching it.",
    "Amazing performance by the actors, highly recommended.",
    "Complete waste of time, boring and long.",
    "One of the best movies I've seen, truly captivating!"
]

# Clean the new reviews (use the same cleaning function you applied before)
new_reviews_cleaned = [clean_text(review) for review in new_reviews]

# Transform the new reviews using the same TF-IDF vectorizer
new_reviews_tfidf = tfidf_vectorizer.transform(new_reviews_cleaned)

# Predict the sentiment of the new reviews
new_predictions = nb_model.predict(new_reviews_tfidf)

# Print the predictions
for review, prediction in zip(new_reviews, new_predictions):
    sentiment = "positive" if prediction == 1 else "negative"
    print(f"Review: {review}\nSentiment: {sentiment}\n")

"""# **Using Predefined Models**"""

from textblob import TextBlob

# Sample reviews
reviews = [
    "This movie was amazing! I loved every bit of it.",
    "Worst movie ever, a total waste of time.",
    "It was okay, not great, but not bad either."
]

# Loop through each review and determine the sentiment
for review in reviews:
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print(f"Review: {review} --> Positive Sentiment")
    elif sentiment < 0:
        print(f"Review: {review} --> Negative Sentiment")
    else:
        print(f"Review: {review} --> Neutral Sentiment")
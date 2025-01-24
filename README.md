# 🎬 Movie Reviews Sentiment Analysis

## 📝 Project Overview
In this project, we built a sentiment analysis model to classify movie reviews as positive or negative using machine learning 🤖. 
The model is trained on a dataset of movie reviews, processes the text data, and provides insights into the sentiment of the reviews.

---

## 🔄 Workflow

1. **Dataset Loading 📂**  
   We started by loading the movie reviews dataset containing textual data and corresponding sentiment labels (positive or negative). The dataset was loaded into a Pandas DataFrame for easy manipulation and analysis.

2. **Data Preprocessing 🔧**  
   Data preprocessing is a crucial step in NLP tasks. The following operations were performed:
   
   - **Tokenization 📝**: We broke down the reviews into individual words or tokens for analysis, enabling the model to understand each word.
   - **Stopword Removal 🚫**: Common words such as "the", "is", "in" were removed, as they do not contribute significant meaning to the sentiment.
   - **Lemmatization 🌿**: Words were reduced to their base form (e.g., "running" becomes "run") to standardize the text and improve model efficiency.

3. **Text Vectorization 📊**  
   To convert the text data into a format the machine learning model can understand, we used **TF-IDF (Term Frequency-Inverse Document Frequency)**. This technique helps to weigh the words based on their importance in the entire dataset, focusing on unique and relevant terms.

4. **Splitting Data 📉📈**  
   We divided the data into two parts:
   - **Training Set 🏋️**: Used to train the model (80% of the data).
   - **Testing Set 🧪**: Used to evaluate the model's performance (20% of the data).

5. **Model Building 🏗️**  
   We built a machine learning model using **Logistic Regression** (a popular algorithm for binary classification). The model is designed to learn patterns in the data to predict sentiment based on the words used in the review.

6. **Training the Model 🚀**  
   The model was trained using the training dataset. During training, the model adjusted its parameters to minimize errors and improve its predictions. We used **accuracy** as the evaluation metric to track how well the model was performing during training.

7. **Model Evaluation 📊**  
   After training, the model was tested on the testing set to evaluate its performance. We calculated the **accuracy** to determine how well the model could classify new, unseen data into positive or negative sentiments. 

   **Accuracy**: The model achieved **88% accuracy** 🎯 on the test dataset, indicating a high level of performance in predicting the sentiment of movie reviews correctly.

8. **Saving the Model 💾**  
   Once we achieved satisfactory results with 88% accuracy, we saved the trained model using **pickle** or **joblib**. This allows us to reuse the model for predictions without retraining it, saving time and computational resources.

9. **Testing the Model 🧪**  
   The final step involved testing the saved model on new, unseen movie reviews. The model provided predictions for these reviews, which were compared with the actual labels to assess its real-world performance. The predictions showed that the model could accurately predict the sentiment of new reviews.

## 📈 Results
- **Accuracy**: The model achieved **88% accuracy** 🎯, which means it correctly predicted the sentiment (positive or negative) of movie reviews 88% of the time.
- **Model Performance**: The model demonstrated strong performance, with good classification boundaries between positive and negative reviews, making it effective in understanding audience sentiment.

---

## 📂 Final Thoughts
This project showcases the use of machine learning for text classification and provides a robust workflow for processing text data, building a model, and evaluating its performance. With an accuracy of 88%, the model can be confidently used for sentiment analysis on movie reviews.

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/N-BHANUTEJA/movie-reviews-sentiment-analysis.git

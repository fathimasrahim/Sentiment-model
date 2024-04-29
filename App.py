import streamlit as st
import joblib


# Load the trained model
model = joblib.load("sentiment-model.pkl")

# Define sentiment labels
sentiment_labels = {'1': 'Positive', '0': 'Negative'}

# Create Streamlit app
st.title("Sentiment Analysis")

# Input text area
user_input = st.text_area('Enter your thoughts here')

# Prediction button
if st.button("Predict"):
    predicted_sentiment = model.predict([user_input])[0]
    predicted_sentiment_label = sentiment_labels[str(predicted_sentiment)]

    # Display predicted sentiment
    st.info(f"Predicted Sentiment: {predicted_sentiment_label}")
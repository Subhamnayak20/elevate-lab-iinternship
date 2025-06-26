import streamlit as st
import pickle

# Load saved files
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("📰 Fake News Classifier")
st.write("Enter any news article below to check if it's REAL or FAKE.")

# User input
news_input = st.text_area("📝 News Text", height=200)

# Predict
if st.button("Predict"):
    if news_input.strip() == "":
        st.warning("Please enter some news text.")
    else:
        vectorized = vectorizer.transform([news_input])
        prediction = model.predict(vectorized)[0]
        label_map = {0: "REAL", 1: "FAKE"}  # Change if your labels are flipped
        st.success(f"🧠 Prediction: **{label_map[prediction]}**")
